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
