"""Evaluation metrics (proposal Section 3.2.8), computed per message.

The attack class (label 1) is the positive class.

    accuracy   = (TP + TN) / (TP + TN + FP + FN)
    precision  = TP / (TP + FP)
    recall     = TP / (TP + FN)
    F1-score   = 2 * precision * recall / (precision + recall)
    FPR        = FP / (FP + TN)         false alarms per attack-free frame
    retention  = F1 cross-vehicle (test_02) / F1 same-vehicle (test_01)
"""
from __future__ import annotations

import numpy as np


def confusion(y_true, y_pred) -> dict[str, int]:
    y_true = np.asarray(y_true).astype(int)
    y_pred = np.asarray(y_pred).astype(int)
    return {
        "TP": int(((y_true == 1) & (y_pred == 1)).sum()),
        "FP": int(((y_true == 0) & (y_pred == 1)).sum()),
        "TN": int(((y_true == 0) & (y_pred == 0)).sum()),
        "FN": int(((y_true == 1) & (y_pred == 0)).sum()),
    }


def _div(a, b) -> float:
    return float(a) / float(b) if b else 0.0


def detection_metrics(y_true, y_pred) -> dict[str, float]:
    c = confusion(y_true, y_pred)
    total = sum(c.values())
    precision = _div(c["TP"], c["TP"] + c["FP"])
    recall = _div(c["TP"], c["TP"] + c["FN"])
    return {**c,
            "accuracy": _div(c["TP"] + c["TN"], total),
            "precision": precision,
            "recall": recall,
            "f1": _div(2 * precision * recall, precision + recall),
            "fpr": _div(c["FP"], c["FP"] + c["TN"]),
            "attack_share": _div(c["TP"] + c["FN"], total)}


def retention(f1_cross: float, f1_same: float) -> float:
    return _div(f1_cross, f1_same)
