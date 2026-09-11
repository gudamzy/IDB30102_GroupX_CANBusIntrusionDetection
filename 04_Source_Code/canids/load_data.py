"""Load labelled CAN capture files into one common schema.

Target schema (one row per CAN frame, sorted by time):
    timestamp       float, seconds
    arbitration_id  int (11-bit or 29-bit identifier)
    dlc             int, 0-8
    b0 .. b7        int, 0-255 (missing bytes padded with 0)
    label           int, 1 = attack frame, 0 = attack-free frame
    source_file     str, file the row came from

The loader accepts the column names used by can-train-and-test
(Lampe & Meng, 2024) and by the HCRL datasets. Column names are matched
case-insensitively, so confirm the header of the downloaded files and add
an alias below if a name differs.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

COLUMN_ALIASES = {
    "timestamp": ["timestamp", "time", "ts"],
    "arbitration_id": ["arbitration_id", "can_id", "id", "arbitration id"],
    "data_field": ["data_field", "data", "payload"],
    "dlc": ["dlc"],
    "label": ["attack", "label", "class", "flag"],
}

BYTE_COLS = [f"b{i}" for i in range(8)]


def _find_column(columns: Iterable[str], wanted: str) -> str | None:
    lookup = {c.strip().lower(): c for c in columns}
    for alias in COLUMN_ALIASES[wanted]:
        if alias in lookup:
            return lookup[alias]
    return None


def _parse_id(value) -> int:
    text = str(value).strip().lower().replace("0x", "")
    return int(text, 16)


def _parse_payload(value) -> list[int]:
    """Turn '0A1B2C' or '0a 1b 2c' into a list of up to 8 byte values."""
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return []
    text = str(value).strip().replace(" ", "")
    if len(text) % 2:
        text = "0" + text
    return [int(text[i:i + 2], 16) for i in range(0, min(len(text), 16), 2)]


def _parse_label(value) -> int:
    text = str(value).strip().lower()
    return 0 if text in {"0", "0.0", "normal", "r", "benign"} else 1


def load_capture(path: str | Path) -> pd.DataFrame:
    """Load one CSV capture and return it in the common schema."""
    path = Path(path)
    raw = pd.read_csv(path, dtype=str)   # keep hex IDs such as '316' as text
    cols = {k: _find_column(raw.columns, k) for k in COLUMN_ALIASES}
    missing = [k for k in ("timestamp", "arbitration_id", "data_field", "label") if cols[k] is None]
    if missing:
        raise ValueError(f"{path.name}: cannot find columns {missing}; header is {list(raw.columns)}")

    payloads = raw[cols["data_field"]].map(_parse_payload)
    out = pd.DataFrame({
        "timestamp": raw[cols["timestamp"]].astype(float),
        "arbitration_id": raw[cols["arbitration_id"]].map(_parse_id).astype(np.int64),
    })
    if cols["dlc"] is not None:
        out["dlc"] = raw[cols["dlc"]].astype(float).astype(int)
    else:
        out["dlc"] = payloads.map(len).astype(int)

    padded = np.zeros((len(raw), 8), dtype=np.int64)
    for row, values in enumerate(payloads):
        padded[row, :len(values)] = values
    out[BYTE_COLS] = padded
    out["label"] = raw[cols["label"]].map(_parse_label).astype(int)
    out["source_file"] = path.name
    return out.sort_values("timestamp", kind="stable").reset_index(drop=True)


def load_folder(folder: str | Path, pattern: str = "*.csv") -> list[pd.DataFrame]:
    """Load every capture in a folder as a separate DataFrame.

    Captures are kept separate on purpose: timing features must be computed
    within one continuous capture, never across the boundary of two files.
    """
    files = sorted(Path(folder).glob(pattern))
    if not files:
        raise FileNotFoundError(f"No files matching {pattern} in {folder}")
    return [load_capture(f) for f in files]
