"""Plot same-vehicle versus cross-vehicle F1-score and FPR for each model."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--results", required=True)
    p.add_argument("--title", default="Same-vehicle vs cross-vehicle")
    a = p.parse_args()
    folder = Path(a.results)
    df = pd.read_csv(folder / "results_per_condition.csv")
    models = ["RF", "DT", "SVM"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, metric, label in [(axes[0], "f1", "F1-score (attack class)"), (axes[1], "fpr", "False-positive rate")]:
        for i, (cond, name, color) in enumerate([("same_vehicle", "Same vehicle", "#1F4E9C"), ("cross_vehicle", "Cross vehicle", "#3DA5E0")]):
            vals = [df[(df.model == m) & (df.condition == cond)][metric].mean() for m in models]
            bars = ax.bar([k + (i - 0.5) * 0.38 for k in range(3)], vals, 0.38, label=name, color=color)
            ax.bar_label(bars, fmt="%.2f", fontsize=8)
        ax.set_xticks(range(3)); ax.set_xticklabels(["Random Forest", "Decision Tree", "SVM"])
        ax.set_ylim(0, 1.3); ax.set_ylabel(label); ax.legend(fontsize=8, ncol=2, loc="upper center")
    fig.suptitle(a.title); fig.tight_layout()
    fig.savefig(folder / "f1_fpr_same_vs_cross.png", dpi=150)
    print("saved", folder / "f1_fpr_same_vs_cross.png")


if __name__ == "__main__":
    main()
