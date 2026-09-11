# Literature Review Summary

## CAN Bus Security
The Controller Area Network (CAN) is widely used for communication between electronic control units in vehicles. However, the CAN protocol was originally designed without strong security mechanisms, making it vulnerable to attacks such as message injection and manipulation.

## Machine Learning-Based Intrusion Detection
Machine learning has been widely studied for detecting malicious CAN bus traffic. Models such as Random Forest, Decision Tree, and Support Vector Machine can learn patterns from CAN traffic and classify normal and malicious activities.

## Deep Learning Approaches
Deep learning approaches have also been proposed for CAN bus intrusion detection. These methods can provide strong detection performance, but they may require more computational resources and training data compared with traditional machine learning models.

## Multi-Vehicle Evaluation
A major limitation identified in previous studies is that many intrusion detection models are evaluated using data from the same vehicle or dataset used during model development. This does not clearly show whether the models can generalise to CAN traffic from different vehicles.

## Research Gap
The literature review identified two main research gaps:

1. Limited evaluation of intrusion detection models across different vehicles.
2. Inconsistent evaluation approaches, including differences in datasets, preprocessing methods, and performance metrics.

The proposed research addresses these gaps by evaluating Random Forest, Decision Tree, and Support Vector Machine under the same experimental conditions using multi-vehicle CAN bus data.

## Comparison of Related Studies

| Study | Method | Dataset / Vehicle | Main Finding | Limitation / Relevance |
|---|---|---|---|---|
| Alalwany & Mahgoub (2022) | Random Forest, XGBoost, KNN and other ML methods | CAN network data | RF and XGBoost showed strong performance | Mainly focused on known attacks |
| Bari et al. (2023) | Decision Tree and other ML algorithms | Kia Soul and Chevrolet Spark | Approximately 99.4%–99.9% performance | Limited evidence of cross-vehicle generalisation |
| Ben Othmane et al. (2022) | K-means and Hidden Markov Model | Moving Ford Transit | Detection performance was lower under realistic vehicle conditions | High false-positive rate |
| Cheng et al. (2022) | TCAN-IDS | CAN attack data | F1-score up to 99.98% | Uses window-based evaluation |
| Dasari & Gottumukkala (2024) | Improved Random Forest | IoV / CAN data | Around 0.99 performance | Limited cross-vehicle testing |
| Wu et al. (2023) | ConvLSTM | CAN bus data | Around 99.95% performance | More complex deep learning approach |
| Xiao et al. (2024) | Graph node attention | Hyundai and Chevrolet | Accuracy dropped from 0.957 to 0.615 | Shows cross-vehicle generalisation problem |
| Lampe & Meng (2024) | Multi-vehicle CAN dataset | 4 vehicles, 2 manufacturers | Supports multi-vehicle IDS evaluation | Suitable for cross-vehicle testing |

## Connection to Proposed Research

The comparison shows that many previous studies achieved high intrusion detection performance, but cross-vehicle evaluation remains limited. Differences in datasets and evaluation methods also make direct comparison difficult. Therefore, the proposed research will evaluate Random Forest, Decision Tree, and Support Vector Machine using multi-vehicle CAN bus data under the same experimental conditions.
