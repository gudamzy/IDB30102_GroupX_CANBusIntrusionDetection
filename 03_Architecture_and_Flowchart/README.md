# Architecture and Flowchart

This folder contains the proposed research architecture and flowchart for evaluating the cross-vehicle performance of machine learning-based intrusion detection models for automotive CAN bus networks.

## Figure 3.1 – Proposed Research Architecture

The proposed architecture begins with a multi-vehicle CAN bus dataset followed by data preprocessing. The processed data will be used to train and evaluate three machine learning models: Random Forest, Decision Tree, and Support Vector Machine.

Two evaluation settings will be used: same-vehicle evaluation as the baseline and cross-vehicle evaluation to examine model generalisation. The models will be evaluated using accuracy, precision, recall, F1-score, and false-positive rate. The final stage compares the performance of the models across different vehicle data.

## Figure 3.2 – Proposed Research Flowchart

The research flowchart shows the experimental process from dataset preparation until performance analysis. After obtaining and preprocessing the CAN bus data, relevant features and labels will be prepared for model training.

Random Forest, Decision Tree, and Support Vector Machine will first undergo same-vehicle evaluation. Cross-vehicle evaluation will then be performed by testing the trained models using data from different vehicles. The resulting performance metrics will be compared to determine how well each model generalises across vehicles.

## Files

- `Figure_3.1_Proposed_Research_Architecture.png` – Proposed research architecture.
- `Figure_3.2_Proposed_Research_Flowchart.jpg` – Proposed research flowchart.
