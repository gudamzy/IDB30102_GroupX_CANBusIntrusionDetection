# Dataset Information

## Selected Dataset
can-train-and-test

## Source
Lampe and Meng (2024)

## Purpose
The dataset is selected because it supports the evaluation of CAN bus intrusion detection models across multiple vehicles.

## Dataset Characteristics
The can-train-and-test dataset contains:
- CAN bus traffic from four vehicles
- Vehicles from two different manufacturers
- Normal CAN traffic
- Multiple malicious attack scenarios
- Nine attack types

## Relevance to This Research
The proposed research focuses on cross-vehicle evaluation. Therefore, a dataset containing CAN traffic from more than one vehicle is required.

The dataset will support two main experimental settings:

1. Same-vehicle evaluation  
   The model is trained and tested using data from the same vehicle.

2. Cross-vehicle evaluation  
   The model is trained using data from one vehicle and tested using data from another vehicle.

This makes the dataset suitable for studying whether machine learning-based intrusion detection models can generalise across different vehicles.

## Planned Use
The dataset will be used for:
- Data preprocessing
- Feature preparation
- Model training
- Same-vehicle testing
- Cross-vehicle testing
- Performance comparison

The full dataset is not included in this repository due to dataset size. Dataset information and sample input may be stored here instead.
