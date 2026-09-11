# Data or Sample Input

This folder contains information and sample input related to the CAN bus dataset that will be used in the proposed research.

## Proposed Dataset

The proposed research will use the **can-train-and-test** dataset introduced by Lampe and Meng (2024). The dataset contains CAN bus data from four vehicles from two manufacturers and includes nine attack types.

The multi-vehicle structure makes the dataset suitable for evaluating whether machine learning-based intrusion detection models can maintain their performance when tested using data from different vehicles.

## Intended Use

The dataset will be used to:

- Prepare normal and malicious CAN bus traffic for machine learning.
- Train Random Forest, Decision Tree, and Support Vector Machine models.
- Perform same-vehicle evaluation as the baseline.
- Perform cross-vehicle evaluation using different vehicle data.
- Compare model performance using accuracy, precision, recall, F1-score, and false-positive rate.

## Files

- `dataset_information.md` – Contains information about the proposed dataset, source, reference, and its use in the research.
- `sample_can_input.csv` – Provides a small sample of the expected CAN bus input structure for preliminary development.

## Note

The sample CSV file is provided only to demonstrate the expected data structure. It is not presented as actual data extracted from the can-train-and-test dataset. The full dataset will be prepared and used during the experimental stage of the research.
