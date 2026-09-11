# 06_Results_or_Expected_Output

At proposal stage this folder holds the expected output format and a pipeline smoke test. No results on the real dataset exist yet.

| Item | Content |
|---|---|
| `expected_results_template.csv` | Table 3.1 in the format the experiment will fill: 3 models × 2 conditions × 4 sub-datasets = 24 rows |
| `smoke_test/` | Output on **synthetic** data: `results_per_condition.csv`, `retention_summary.csv`, `f1_fpr_same_vs_cross.png` |

## Smoke test (synthetic data, not a research result)

| Model | F1 same vehicle | F1 cross vehicle | FPR cross vehicle |
|---|---|---|---|
| Random Forest | 1.000 | 0.511 | 0.999 |
| Decision Tree | 0.999 | 0.510 | 0.998 |
| SVM (linear) | 0.989 | 0.955 | 0.042 |

The synthetic vehicles were generated with non-overlapping ID ranges, so tree models that split on the ID value flag
almost every frame of the second vehicle as an attack. This only confirms that the pipeline computes every metric and
chart. It says nothing about real vehicles.

## Metrics (Section 3.2.8)

| Metric | Definition |
|---|---|
| Accuracy | (TP + TN) / all frames |
| Precision | TP / (TP + FP) |
| Recall | TP / (TP + FN) |
| F1-score | 2 × precision × recall / (precision + recall) |
| False-positive rate | FP / (FP + TN) |
| F1 retention | cross-vehicle F1 / same-vehicle F1 |

Because attack frames are a small share of each subset, F1-score and false-positive rate are the main measures.

## Success criteria

A model generalises well if its cross-vehicle F1-score is at least 90% of its same-vehicle F1-score in at least three of
the four sub-datasets, and its cross-vehicle false-positive rate is 1% or lower. `retention_summary.csv` reports this per
model and sub-dataset in the `meets_criteria` column.

## Expected outcome

A comparison of Random Forest, Decision Tree and SVM showing how much each model's performance changes between
same-vehicle and cross-vehicle data, and which model is most consistent.
