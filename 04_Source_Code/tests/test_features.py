"""Unit tests for feature extraction."""
import numpy as np
import pandas as pd

from canids.features import FEATURE_COLUMNS, extract_features
from canids.load_data import BYTE_COLS


def _capture(rows):
    df = pd.DataFrame(rows, columns=["timestamp", "arbitration_id"] + BYTE_COLS + ["label"])
    df["dlc"] = 8
    return df.sort_values("timestamp").reset_index(drop=True)


def test_feature_columns():
    assert FEATURE_COLUMNS == ["arbitration_id", "dlc"] + BYTE_COLS + ["dt_id"]


def test_time_since_previous_frame_of_same_id():
    z = [0] * 8
    f = extract_features(_capture([(0.00, 0x100, *z, 0), (0.01, 0x200, *z, 0), (0.10, 0x100, *z, 0)]))
    assert f.loc[0, "dt_id"] == 1.0                 # first time the ID is seen
    assert f.loc[1, "dt_id"] == 1.0
    assert abs(f.loc[2, "dt_id"] - 0.10) < 1e-9


def test_features_are_causal():
    """Appending later frames must not change features of earlier frames."""
    rng = np.random.default_rng(0)
    rows = [(i * 0.01, int(rng.integers(1, 4)), *rng.integers(0, 256, 8), 0) for i in range(50)]
    full = extract_features(_capture(rows))
    part = extract_features(_capture(rows[:30]))
    pd.testing.assert_frame_equal(full.iloc[:30].reset_index(drop=True), part, check_dtype=False)
