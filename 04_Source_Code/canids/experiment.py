"""Same-vehicle and cross-vehicle experiment (proposal Section 3.2.5).

For each can-train-and-test sub-dataset:
    Stage 3  train Random Forest, Decision Tree and Support Vector Machine on
             the same stratified sample of train_01
    Stage 4  test on test_01 (same vehicle)
    Stage 5  test on test_02 (cross vehicle)
Controls: identical features, identical training sample, fixed random seed,
no class balancing on the test data.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier

from .features import build_matrix
from .load_data import load_folder
from .metrics import detection_metrics, retention

SUBSETS = {
    "same_vehicle": "test_01_known_vehicle_known_attack",
    "cross_vehicle": "test_02_unknown_vehicle_known_attack",
}
SEED = 42
TRAIN_SAMPLE = 500_000


def make_model(name: str):
    if name == "RF":
        return RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=SEED)
    if name == "DT":
        return DecisionTreeClassifier(random_state=SEED)
    if name == "SVM":
        # Linear kernel: a kernel SVM does not scale to hundreds of thousands of frames.
        return make_pipeline(StandardScaler(), LinearSVC(dual=False, random_state=SEED, max_iter=5000))
    raise ValueError(name)


def stratified_sample(X: pd.DataFrame, y: np.ndarray, n: int, seed: int = SEED):
    """Keep the attack share of the training data while limiting its size."""
    if len(y) <= n:
        return X, y
    rng = np.random.default_rng(seed)
    idx = []
    for label in (0, 1):
        pool = np.flatnonzero(y == label)
        k = int(round(n * len(pool) / len(y)))
        idx.append(rng.choice(pool, size=min(k, len(pool)), replace=False))
    idx = np.sort(np.concatenate(idx))
    return X.iloc[idx].reset_index(drop=True), y[idx]


def run_set(set_dir: str | Path, models=("RF", "DT", "SVM"), train_sample: int = TRAIN_SAMPLE) -> pd.DataFrame:
    set_dir = Path(set_dir)
    X_train, y_train = build_matrix(load_folder(set_dir / "train_01"))
    X_train, y_train = stratified_sample(X_train, y_train, train_sample)
    tests = {cond: build_matrix(load_folder(set_dir / folder)) for cond, folder in SUBSETS.items()}

    rows = []
    for m in models:
        model = make_model(m).fit(X_train, y_train)
        for cond, (X_test, y_test) in tests.items():
            row = {"set": set_dir.name, "model": m, "condition": cond,
                   "train_rows": len(y_train), "train_attack_share": float(y_train.mean()),
                   "test_rows": len(y_test)}
            row.update(detection_metrics(y_test, model.predict(X_test)))
            rows.append(row)
    return pd.DataFrame(rows)


def retention_table(results: pd.DataFrame) -> pd.DataFrame:
    """Same-vehicle F1, cross-vehicle F1, retention and cross-vehicle FPR per model."""
    f1 = results.pivot_table(index=["set", "model"], columns="condition", values="f1").reset_index()
    fpr = results[results.condition == "cross_vehicle"][["set", "model", "fpr"]].rename(columns={"fpr": "fpr_cross"})
    out = f1.merge(fpr, on=["set", "model"])
    out["retention"] = [retention(c, s) for c, s in zip(out["cross_vehicle"], out["same_vehicle"])]
    out["meets_criteria"] = (out["retention"] >= 0.90) & (out["fpr_cross"] <= 0.01)
    return out
