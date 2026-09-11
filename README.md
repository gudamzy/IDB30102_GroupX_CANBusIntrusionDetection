# Evaluating the Cross-Vehicle Performance of Machine Learning-Based Intrusion Detection Models for Automotive CAN Bus Networks

**IDB30102 Research Methodology · Assignment 2 · UniKL MIIT · July 2026 Semester**

| Item | Details |
|---|---|
| **Group** | Group X |
| **Assigned Research Area** | Automotive and Vehicle Security (CAN bus; connected and autonomous vehicles; vehicle forensics) |
| **Lecturer** | Dr. Delina Beh Mei Yin |

## Group Members

| No. | Member | Student ID |
|---:|---|---|
| 1 | Muhammad Adam Danish bin Mohd Anis | 52215125900 |
| 2 | Mohamad Syahmi Amrin bin Mursham | 52215125622 |
| 3 | Muhammad Muttakin bin Mat Hussin | 52215226045 |
| 4 | Muhammad Imran Zafri bin Mohd Suhaini | 52215226113 |

## Research Problem

### Limited Cross-Vehicle Evaluation

Most CAN bus IDS studies train and test using data from the same dataset or vehicle. CAN identifiers and message patterns can differ between vehicle models and manufacturers, which means a model may learn characteristics that are specific to the training vehicle.

Xiao et al. (2024) reported an accuracy decrease from **0.957 on Hyundai data to 0.615 on Chevrolet data**, highlighting the importance of evaluating IDS models across different vehicles.

### Inconsistent Evaluation

Existing studies use different datasets, attack distributions, preprocessing methods, labelling approaches, and testing environments. Some studies also do not report the false-positive rate (FPR), making direct comparison between models difficult.

## Research Aim

To evaluate the cross-vehicle performance of machine learning-based intrusion detection models for automotive CAN bus networks.

## Research Objectives

**RO1:** To identify suitable machine learning techniques and multi-vehicle CAN bus data for automotive intrusion detection.

**RO2:** To implement selected machine learning models for detecting normal and malicious CAN bus traffic.

**RO3:** To evaluate and compare the performance of the selected models on same-vehicle and cross-vehicle test data using accuracy, precision, recall, F1-score, and false-positive rate.

## Proposed Solution

Three machine learning models are evaluated:

- Random Forest (RF)
- Decision Tree (DT)
- Support Vector Machine (SVM) with a linear kernel

The models are trained using the same features and the same stratified sample of **500,000 frames** from `train_01` of each `can-train-and-test` sub-dataset.

Each trained model is then evaluated using:

- `test_01` — same-vehicle testing (baseline)
- `test_02` — cross-vehicle testing using a vehicle not included in training

The features extracted from each CAN frame are:

- Arbitration ID
- Data Length Code (DLC)
- Eight CAN data bytes
- Time since the previous frame with the same ID

## Methodology

| Layer | Choice |
|---|---|
| **Research Methodology** | Experimental (Wohlin et al., 2012): dataset preparation → preprocessing → model implementation → same-vehicle evaluation → cross-vehicle evaluation → performance comparison |
| **Development Model** | Not applicable — the Python scripts support the experiment and are not intended to form a complete software system |

## Proposed Evaluation Plan

| Item | Plan |
|---|---|
| **Baseline** | Same-vehicle result (`test_01`) for each model |
| **Dataset** | `can-train-and-test` (Lampe & Meng, 2024), `set_01`–`set_04`, representing four vehicles from two manufacturers |
| **Test Environment** | Offline experiment using Python and scikit-learn on a laptop |
| **Metrics** | Accuracy, Precision, Recall, F1-score, False-Positive Rate (FPR) |
| **Additional Measure** | F1 Retention = Cross-Vehicle F1 / Same-Vehicle F1 |
| **Success Criteria** | Cross-vehicle F1 ≥ 90% of same-vehicle F1 in at least 3 of 4 sub-datasets, and cross-vehicle FPR ≤ 1% |

## Proposed Architecture

![Proposed Architecture](03_Architecture_and_Flowchart/architecture.jpeg)

## Repository Contents

| Folder | Content |
|---|---|
| `01_Research_Papers/` | Information on papers cited in Chapter 2, including DOI information |
| `02_Literature_Review/` | Table 2.1, technique comparison, research gap, datasets, and evaluation metrics |
| `03_Architecture_and_Flowchart/` | Figures 3.1–3.3 of the research proposal |
| `04_Source_Code/` | Data loader, feature processing, metrics, experiment runner, and unit tests |
| `05_Data_or_Sample_Input/` | Dataset description and link, together with synthetic sample captures |
| `06_Results_or_Expected_Output/` | Expected results template, smoke-test output, and success criteria |
| `07_References/` | APA references, dataset references, and library references |

## Mapping Technical Work to Research Objectives

| Objective | Supporting Component | GitHub Location |
|---|---|---|
| **RO1 — Identify techniques and multi-vehicle data** | Paper summaries, Table 2.1, dataset comparison | `01_Research_Papers/`, `02_Literature_Review/`, `05_Data_or_Sample_Input/` |
| **RO2 — Implement RF, DT and SVM** | Architecture, flowchart, `load_data.py`, `features.py`, `experiment.py` | `03_Architecture_and_Flowchart/`, `04_Source_Code/` |
| **RO3 — Evaluate same-vehicle vs cross-vehicle performance** | `metrics.py`, results template, smoke test | `04_Source_Code/`, `06_Results_or_Expected_Output/` |

## Tools

- Python 3
- pandas
- NumPy
- scikit-learn
- matplotlib
- pytest
- `can-train-and-test` dataset

## Running the Preliminary Code

```bash
cd 04_Source_Code

pip install -r requirements.txt

python -m pytest -q tests

python make_synthetic_data.py

python run_experiment.py \
    --data-root ../05_Data_or_Sample_Input/synthetic \
    --sets set_syn \
    --out ../06_Results_or_Expected_Output/smoke_test

python plot_results.py \
    --results ../06_Results_or_Expected_Output/smoke_test
```

The synthetic captures are used **for testing the experimental pipeline only** and are not used for the final model evaluation.

For instructions on running the experiment using the real dataset, refer to `04_Source_Code/README.md`.

## Ethics

All experiments are conducted offline using a public dataset. No real vehicle or third-party system is actively tested, and no human participants are involved.

The original dataset is linked rather than redistributed through this repository.

## Licence

The source code is released under the **MIT License**. See `LICENSE` for details.

Research papers and datasets remain the property of their respective authors and are cited in `07_References/`.
