# Research Paper Analysis

This file summarises important research papers used to support the proposed study on cross-vehicle performance of machine learning-based intrusion detection models for automotive CAN bus networks.

## Paper 1

**Title:** Classification of Normal and Malicious Traffic Based on an Ensemble of Machine Learning for a Vehicle CAN-Network

**Authors:** E. Alalwany and I. Mahgoub

**Year:** 2022

**Research Problem:**  
The study investigates the detection and classification of normal and malicious traffic in automotive CAN networks using machine learning.

**Method / Technique:**  
Several machine learning techniques were evaluated, including Random Forest, XGBoost, K-Nearest Neighbour and other machine learning methods.

**Dataset / Tools:**  
CAN network traffic data.

**Main Findings:**  
Random Forest and XGBoost showed strong intrusion detection performance.

**Limitation:**  
The study mainly focused on detecting known attacks and did not provide strong evidence of cross-vehicle generalisation.

**Relevance to Proposed Research:**  
This study supports the selection of Random Forest as one of the machine learning models to be evaluated in the proposed research.

---

## Paper 2

**Title:** Intrusion Detection in Vehicle Controller Area Network (CAN) Bus Using Machine Learning: A Comparative Performance Study

**Authors:** B. S. Bari, K. Yelamarthi, and S. Ghafoor

**Year:** 2023

**Research Problem:**  
The study compares machine learning algorithms for identifying malicious activities in automotive CAN bus communication.

**Method / Technique:**  
Decision Tree and other machine learning classification algorithms were evaluated.

**Dataset / Tools:**  
CAN bus traffic from Kia Soul and Chevrolet Spark vehicles.

**Main Findings:**  
The evaluated machine learning methods achieved approximately 99.4% to 99.9% performance.

**Limitation:**  
Although data from different vehicle models were used, there was limited evidence showing whether models trained on one vehicle could generalise well to another vehicle.

**Relevance to Proposed Research:**  
The study supports the use of Decision Tree and shows the importance of evaluating machine learning performance using data from different vehicles.

---

## Paper 3

**Title:** On the Performance of Detecting Injection of Fabricated Messages into the CAN Bus

**Authors:** L. Ben Othmane, L. Dhulipala, M. Abdelkhalek, N. Multari, and M. Govindarasu

**Year:** 2022

**Research Problem:**  
The study evaluates methods for detecting fabricated message injection attacks in automotive CAN bus networks under realistic vehicle conditions.

**Method / Technique:**  
K-means clustering and Hidden Markov Model approaches were evaluated.

**Dataset / Tools:**  
CAN traffic collected from a moving Ford Transit vehicle.

**Main Findings:**  
The k-means approach detected approximately 71% to 79% of attacks, while the Hidden Markov Model achieved approximately 75% to 80% detection performance.

**Limitation:**  
The approaches produced relatively high false-positive rates. Real vehicle testing reported false-positive rates of approximately 42.5% to 68%.

**Relevance to Proposed Research:**  
This study shows that high performance reported using controlled datasets may not always be maintained under realistic vehicle conditions. It also supports including false-positive rate as an evaluation metric.

---

## Paper 4

**Title:** A Novel Feature Extraction Framework Using Graph Node Attention Network for In-Vehicle Networks Intrusion Detection

**Authors:** J. Xiao, H. Chen, and F. Zhong

**Year:** 2024

**Research Problem:**  
The study investigates intrusion detection in in-vehicle networks and evaluates whether the proposed approach can maintain its performance across different vehicle data.

**Method / Technique:**  
Graph node attention-based feature extraction and intrusion detection.

**Dataset / Tools:**  
Hyundai and Chevrolet vehicle data.

**Main Findings:**  
The approach achieved approximately 0.957 accuracy using Hyundai data, but the accuracy decreased to approximately 0.615 when evaluated using Chevrolet data.

**Limitation:**  
The large reduction in accuracy shows limited cross-vehicle generalisation.

**Relevance to Proposed Research:**  
This study directly supports the main research gap of the proposed research. It shows that a model that performs well on one vehicle may not maintain the same performance when tested on another vehicle.

---

## Paper 5

**Title:** Can-Train-and-Test: A Curated CAN Dataset for Automotive Intrusion Detection

**Authors:** B. Lampe and W. Meng

**Year:** 2024

**Research Problem:**  
The study addresses the need for broader and more suitable CAN bus datasets for automotive intrusion detection evaluation.

**Method / Technique:**  
Development and organisation of a curated multi-vehicle CAN bus dataset for intrusion detection research.

**Dataset / Tools:**  
The can-train-and-test dataset contains CAN data from four vehicles from two manufacturers and includes nine attack types.

**Main Findings:**  
The dataset provides multi-vehicle CAN bus data that can support broader intrusion detection testing across different vehicle environments.

**Limitation:**  
The dataset provides the data needed for multi-vehicle evaluation, but intrusion detection models still need to be experimentally evaluated to determine their cross-vehicle performance.

**Relevance to Proposed Research:**  
This dataset is suitable for the proposed research because it enables same-vehicle and cross-vehicle evaluation of Random Forest, Decision Tree, and Support Vector Machine models.
