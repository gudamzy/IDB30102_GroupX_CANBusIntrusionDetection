"""Per-message feature extraction (proposal Section 3.2.4).

All three models use the same features for every CAN frame:

    arbitration_id  CAN identifier as an integer
    dlc             data length code
    b0 .. b7        the eight data bytes
    dt_id           seconds since the previous frame with the same ID
                    (causal: uses only earlier frames in the same capture)

Features are computed within one continuous capture at a time, so timing is
never measured across the boundary between two recordings.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .load_data import BYTE_COLS

FEATURE_COLUMNS = ["arbitration_id", "dlc"] + BYTE_COLS + ["dt_id"]
FIRST_SEEN_DT = 1.0   # value used when an ID has no earlier frame in the capture


def extract_features(capture: pd.DataFrame) -> pd.DataFrame:
    df = capture.reset_index(drop=True)
    out = df[["arbitration_id", "dlc"] + BYTE_COLS].copy()
    dt = df["timestamp"] - df.groupby("arbitration_id", sort=False)["timestamp"].shift(1)
    out["dt_id"] = dt.fillna(FIRST_SEEN_DT).clip(upper=FIRST_SEEN_DT)
    return out[FEATURE_COLUMNS]


def build_matrix(captures: list[pd.DataFrame]) -> tuple[pd.DataFrame, np.ndarray]:
    """Extract features from several captures and stack them with per-message labels."""
    xs = [extract_features(c) for c in captures]
    ys = [c["label"].to_numpy() for c in captures]
    return pd.concat(xs, ignore_index=True), np.concatenate(ys)
