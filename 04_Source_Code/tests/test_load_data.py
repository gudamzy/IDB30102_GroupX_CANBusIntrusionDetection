"""Unit tests for the CAN capture loader."""
import pandas as pd

from canids.load_data import load_capture


def test_loader_handles_hex_ids_and_short_payloads(tmp_path):
    p = tmp_path / "cap.csv"
    pd.DataFrame({
        "timestamp": [0.2, 0.1],
        "arbitration_id": ["1A0", "0C1"],
        "data_field": ["0102", "FFEEDDCCBBAA9988"],
        "attack": [1, 0],
    }).to_csv(p, index=False)
    df = load_capture(p)
    assert list(df["arbitration_id"]) == [0x0C1, 0x1A0]        # sorted by time
    assert df.loc[1, "dlc"] == 2 and df.loc[1, "b1"] == 2 and df.loc[1, "b2"] == 0
    assert list(df["label"]) == [0, 1]


def test_loader_accepts_hcrl_style_header(tmp_path):
    p = tmp_path / "hcrl.csv"
    pd.DataFrame({
        "Timestamp": [0.0], "Arbitration_ID": ["316"], "DLC": [8],
        "Data": ["05 21 68 09 21 21 00 6f"], "Class": ["Attack"],
    }).to_csv(p, index=False)
    df = load_capture(p)
    assert df.loc[0, "arbitration_id"] == 0x316 and df.loc[0, "b7"] == 0x6F
    assert df.loc[0, "label"] == 1
