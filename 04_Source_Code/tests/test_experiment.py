"""Unit tests for the training sample and model factory."""
import numpy as np
import pandas as pd

from canids.experiment import make_model, stratified_sample


def test_stratified_sample_keeps_attack_share():
    y = np.array([1] * 100 + [0] * 900)
    X = pd.DataFrame({"a": np.arange(1000)})
    Xs, ys = stratified_sample(X, y, 200)
    assert len(ys) == 200 and abs(ys.mean() - 0.1) < 1e-9


def test_all_three_models_fit():
    rng = np.random.default_rng(0)
    X = pd.DataFrame(rng.normal(size=(200, 3)), columns=list("abc"))
    y = (X["a"] > 0).astype(int).to_numpy()
    for name in ("RF", "DT", "SVM"):
        assert make_model(name).fit(X, y).predict(X).shape == (200,)
