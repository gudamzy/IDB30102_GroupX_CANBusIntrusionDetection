"""Generate SYNTHETIC CAN captures for testing the pipeline end to end.

This data is NOT real vehicle traffic and is NOT used as research evidence.
It exists so that the code in this repository can be executed and checked
without downloading the 1.4 GB can-train-and-test dataset.

Two synthetic "vehicles" are generated with disjoint ID ranges, mimicking
the manufacturer-specific ID assignment that causes cross-vehicle failure:
    vehicle A  IDs in 0x0C0-0x3FF   (used for train_01 and test_01)
    vehicle B  IDs in 0x400-0x7F0   (used for test_02, the "unknown vehicle")

Each capture contains attack-free traffic plus three injected attacks
(DoS, fuzzing, spoofing). The folder layout copies can-train-and-test.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def make_profile(id_low: int, id_high: int, n_ids: int, rng: np.random.Generator) -> list[dict]:
    ids = np.sort(rng.choice(np.arange(id_low, id_high), size=n_ids, replace=False))
    periods = rng.choice([0.01, 0.02, 0.05, 0.1, 0.2, 0.5], size=n_ids, p=[.2, .25, .25, .15, .1, .05])
    profile = []
    for can_id, period in zip(ids, periods):
        profile.append({
            "id": int(can_id),
            "period": float(period),
            "dlc": int(rng.choice([8, 8, 8, 6, 4])),
            "const": rng.integers(0, 256, size=8),
            "signal_freq": float(rng.uniform(0.02, 0.3)),
        })
    return profile


def normal_traffic(profile, duration, rng):
    rows = []
    for p in profile:
        n = int(duration / p["period"])
        t = np.arange(n) * p["period"] + rng.uniform(0, p["period"])
        t = t + rng.normal(0, 0.02 * p["period"], size=n)
        for k, ts in enumerate(t):
            payload = p["const"].copy()
            payload[0] = k % 256                                      # rolling counter
            sig = int(127 + 100 * np.sin(2 * np.pi * p["signal_freq"] * ts))
            payload[1], payload[2] = sig & 0xFF, (sig >> 2) & 0xFF      # slow signal
            rows.append((ts, p["id"], payload[: p["dlc"]], 0))
    return rows


def attacks(profile, duration, rng):
    rows = []
    # DoS: highest-priority ID flooding the bus
    for ts in np.arange(0.30 * duration, 0.40 * duration, 0.0003):
        rows.append((ts, 0x000, np.zeros(8, dtype=int), 1))
    # Fuzzing: random IDs and random payloads
    for ts in np.arange(0.55 * duration, 0.62 * duration, 0.0005):
        rows.append((ts, int(rng.integers(0, 0x800)), rng.integers(0, 256, size=8), 1))
    # Spoofing: a real ID sent 5x faster with a forged, fixed payload
    target = profile[int(rng.integers(0, len(profile)))]
    forged = target["const"].copy()
    forged[1:3] = 0xFF
    for ts in np.arange(0.75 * duration, 0.88 * duration, target["period"] / 5):
        rows.append((ts, target["id"], forged[: target["dlc"]], 1))
    return rows


def write_capture(rows, path: Path):
    rows.sort(key=lambda r: r[0])
    df = pd.DataFrame({
        "timestamp": [round(r[0], 6) for r in rows],
        "arbitration_id": [f"{r[1]:03X}" for r in rows],
        "data_field": ["".join(f"{int(b):02X}" for b in r[2]) for r in rows],
        "attack": [r[3] for r in rows],
    })
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return len(df), int(df["attack"].sum())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="../05_Data_or_Sample_Input/synthetic/set_syn")
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)
    out = Path(args.out)

    vehicle_a = make_profile(0x0C0, 0x400, 25, rng)
    vehicle_b = make_profile(0x400, 0x7F0, 25, rng)

    plan = [
        ("train_01", "vehicleA_mixed_train.csv", vehicle_a, 40),
        ("test_01_known_vehicle_known_attack", "vehicleA_mixed_test.csv", vehicle_a, 30),
        ("test_02_unknown_vehicle_known_attack", "vehicleB_mixed_test.csv", vehicle_b, 30),
    ]
    for folder, name, profile, duration in plan:
        rows = normal_traffic(profile, duration, rng) + attacks(profile, duration, rng)
        n, n_attack = write_capture(rows, out / folder / name)
        print(f"{folder}/{name}: {n} frames, {n_attack} attack ({n_attack / n:.1%})")


if __name__ == "__main__":
    main()
