# Evaluating the Cross-Vehicle Performance of Machine Learning-Based Intrusion Detection Models for Automotive CAN Bus Networks

IDB30102 Research Methodology · Assignment 2 · UniKL MIIT · July 2026 Semester

| Item | Details |
|---|---|
| **Group** | Group X |
| **Assigned Research Area** | Automotive and Vehicle Security |
| **Lecturer** | Dr. Delina Beh Mei Yin |

## Group Members

| No. | Member | Student ID |
|---|---|---|
| 1 | Muhammad Adam Danish bin Mohd Anis | 52215125900 |
| 2 | Mohamad Syahmi Amrin bin Mursham | 52215125622 |
| 3 | Muhammad Muttakin bin Mat Hussin | 52215226045 |
| 4 | Muhammad Imran Zafri bin Mohd Suhaini | 52215226113 |

## Research Problem

Two main issues are addressed in this research.

1. **Limited cross-vehicle evaluation.**  
Many CAN bus intrusion detection studies train and test their models using data from the same dataset or vehicle. However, CAN identifiers and message patterns may differ between vehicle models and manufacturers. Therefore, a model that performs well on one vehicle may not produce the same performance on another vehicle.

2. **Inconsistent evaluation approaches.**  
Previous studies use different datasets, preprocessing methods, class distributions, labelling approaches, hardware environments, and performance metrics. This makes direct comparison between models difficult.

## Research Aim

To evaluate the cross-vehicle performance of machine learning-based intrusion detection models for automotive CAN bus networks.

## Research Objectives

1. **RO1:** To identify suitable machine learning techniques and multi-vehicle CAN bus data for automotive intrusion detection.
2. **RO2:** To implement selected machine learning models for detecting normal and malicious CAN bus traffic.
3. **RO3:** To evaluate and compare the performance of the selected models across different vehicles using accuracy, precision, recall, F1-score, and false-positive rate.

## Proposed Solution

This research evaluates three machine learning models:

- Random Forest
- Decision Tree
- Support Vector Machine

The models will be trained and evaluated using multi-vehicle CAN bus data. Same-vehicle evaluation will first be used as the baseline. Cross-vehicle evaluation will then be performed to determine whether the models can maintain their detection performance when tested using data from different vehicles.

## Research Methodology

| Layer | Selection |
|---|---|
| **Research Methodology** | Experimental Research Methodology |
| **Development Model** | Not applicable |

The Experimental Research Methodology is selected because the study focuses on comparing machine learning models under controlled experimental conditions.

A separate software development model is not required because this research does not develop a complete software system or application. Python scripts are used only to support data preparation, model training, and performance evaluation.

## Proposed Dataset

The proposed dataset is **can-train-and-test** by Lampe and Meng (2024).

The dataset contains CAN bus data from four vehicles and two vehicle manufacturers, including normal and malicious CAN traffic with multiple attack types.

The dataset is suitable for this research because it supports evaluation across different vehicle environments.

## Proposed Evaluation Plan

The evaluation consists of two main stages:

1. **Same-vehicle evaluation** – the model is trained and tested using data from the same vehicle environment. This serves as the baseline.
2. **Cross-vehicle evaluation** – the model is trained using data from one vehicle environment and evaluated using data from a different vehicle environment.

The following performance metrics will be used:

- Accuracy
- Precision
- Recall
- F1-score
- False-positive rate

The results from both evaluation stages will be compared to determine how well each model generalises across different vehicles.

## Proposed Architecture

The proposed research architecture consists of five main stages:

1. Multi-vehicle CAN bus data preparation
2. Data preprocessing
3. Machine learning model implementation
4. Same-vehicle and cross-vehicle evaluation
5. Performance comparison and analysis

The detailed research architecture and flowchart are available in `03_Architecture_and_Flowchart/`.

## Research Objective Mapping

| Research Objective | Supporting Component | GitHub Location |
|---|---|---|
| RO1 | Research papers, literature review, dataset information | `01_Research_Papers/`, `02_Literature_Review/`, `05_Data_or_Sample_Input/` |
| RO2 | Preliminary implementation of Random Forest, Decision Tree, and Support Vector Machine | `04_Source_Code/` |
| RO3 | Same-vehicle and cross-vehicle evaluation, performance metrics, expected results | `04_Source_Code/`, `06_Results_or_Expected_Output/` |

## Repository Structure

- `01_Research_Papers/` – Key research paper summaries and analysis
- `02_Literature_Review/` – Literature review, study comparison and research gap
- `03_Architecture_and_Flowchart/` – Proposed research architecture and flowchart
- `04_Source_Code/` – Preliminary Python implementation
- `05_Data_or_Sample_Input/` – Dataset information and sample CAN bus input
- `06_Results_or_Expected_Output/` – Expected results and evaluation output
- `07_References/` – References and supporting resources

## Tools and Technologies

- Python
- pandas
- NumPy
- scikit-learn
- matplotlib
- pytest
- Jupyter Notebook / Visual Studio Code
- GitHub

## Preliminary Source Code

The current source code is preliminary and demonstrates the planned experimental workflow.

The main scripts include:

- `data_preprocessing.py`
- `train_models.py`
- `evaluation_metrics.py`
- `cross_vehicle_evaluation.py`

Install the required libraries using:

```bash
pip install -r 04_Source_Code/requirements.txt
```

Example execution:

```bash
python 04_Source_Code/data_preprocessing.py
python 04_Source_Code/train_models.py
python 04_Source_Code/evaluation_metrics.py
python 04_Source_Code/cross_vehicle_evaluation.py
```

The complete experimental implementation and final results will be produced during the later research stage.

## Data and Sample Input

The full can-train-and-test dataset is not stored directly in this repository.

The `05_Data_or_Sample_Input/` folder contains:

- Dataset information
- Dataset source and DOI
- Sample CAN bus input structure

The sample input is provided only to demonstrate the expected format and is not extracted from the actual can-train-and-test dataset.

## Expected Output

At the proposal stage, final experimental results are not yet available.

The expected output will compare:

- Random Forest
- Decision Tree
- Support Vector Machine

for both:

- Same-vehicle evaluation
- Cross-vehicle evaluation

The results will be compared using accuracy, precision, recall, F1-score, and false-positive rate.

## Ethics

This research uses a publicly available automotive CAN bus dataset.

The experiments are conducted offline and do not involve:

- Human participants
- Live vehicles
- Third-party systems

The dataset is referenced through its official source and is not redistributed in this repository.

## Licence

The source code in this repository is provided under the MIT License.

Research papers, datasets, and external resources remain the property of their respective authors and are acknowledged in `07_References/`.
