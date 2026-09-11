# 04_Source_Code

Preliminary implementation of the experiment in Chapter 3. Written by Group X; uses the open-source
libraries in `requirements.txt` (BSD licensed). No third-party code has been copied.

| File | Purpose | Proposal stage |
|---|---|---|
| `canids/load_data.py` | Read can-train-and-test (and HCRL-format) CSV files into one per-message table | Stage 1–2 |
| `canids/features.py` | ID, DLC, 8 data bytes, time since previous frame with same ID | Stage 2 |
| `canids/experiment.py` | Stratified 500,000-frame training sample; RF, DT, linear SVM; same- and cross-vehicle tests | Stage 3–5 |
| `canids/metrics.py` | Accuracy, precision, recall, F1-score, FPR, F1 retention | Stage 6 |
| `run_experiment.py` | Command-line entry point | – |
| `plot_results.py` | Same vs cross-vehicle chart | Stage 6 |
| `make_synthetic_data.py` | Synthetic captures for testing the code only | – |
| `tests/` | Unit tests | – |

## Setup and tests

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q tests        # expected: 10 passed
```

## Smoke test (synthetic data)

```bash
python make_synthetic_data.py
python run_experiment.py --data-root ../05_Data_or_Sample_Input/synthetic --sets set_syn --out ../06_Results_or_Expected_Output/smoke_test
python plot_results.py --results ../06_Results_or_Expected_Output/smoke_test
```

The two synthetic vehicles use different ID ranges on purpose. The output only shows the pipeline runs; it is **not** a research result.

## Real dataset

1. Download can-train-and-test: https://data.dtu.dk/articles/dataset/can-train-and-test/24805533 (about 1.4 GB).
2. Unzip outside the repository so the folder contains `set_01` … `set_04`.
3. Open one CSV and check the header; if a column name is missing from `COLUMN_ALIASES` in `load_data.py`, add it.
4. Run:

```bash
python run_experiment.py --data-root ~/data/can-train-and-test --sets set_01 set_02 set_03 set_04 --out ../06_Results_or_Expected_Output/real_run
```

Outputs: `results_per_condition.csv` (Table 3.1 values) and `retention_summary.csv` (success criteria).
