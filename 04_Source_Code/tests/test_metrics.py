"""Unit tests for metric formulas."""
import numpy as np

from canids.metrics import detection_metrics, retention


def test_known_confusion_matrix():
    y_true = np.array([1, 1, 1, 0, 0, 0, 0, 0])
    y_pred = np.array([1, 1, 0, 1, 0, 0, 0, 0])
    m = detection_metrics(y_true, y_pred)
    assert (m["TP"], m["FN"], m["FP"], m["TN"]) == (2, 1, 1, 4)
    assert abs(m["accuracy"] - 6 / 8) < 1e-9
    assert abs(m["precision"] - 2 / 3) < 1e-9
    assert abs(m["recall"] - 2 / 3) < 1e-9
    assert abs(m["fpr"] - 1 / 5) < 1e-9            # FP / (FP + TN)


def test_accuracy_hides_missed_attacks_on_imbalanced_data():
    y_true = np.array([1] + [0] * 99)
    m = detection_metrics(y_true, np.zeros(100))
    assert m["accuracy"] == 0.99 and m["recall"] == 0.0 and m["f1"] == 0.0


def test_retention_ratio():
    assert retention(0.45, 0.9) == 0.5
    assert retention(0.9, 0.0) == 0.0
