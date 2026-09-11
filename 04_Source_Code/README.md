# Source Code

This folder contains the preliminary Python source code for the proposed cross-vehicle evaluation of machine learning-based intrusion detection models for automotive CAN bus networks.

The selected machine learning models are:

- Random Forest (RF)
- Decision Tree (DT)
- Support Vector Machine (SVM)

## Source Code Files

### `data_preprocessing.py`
Handles the preliminary data preprocessing process, including loading CAN bus data, checking missing values, selecting features, and preparing the data for machine learning.

### `train_models.py`
Contains the implementation of Random Forest, Decision Tree, and Support Vector Machine models. The models will be trained using the prepared CAN bus data.

### `evaluation_metrics.py`
Calculates the performance of the machine learning models using accuracy, precision, recall, F1-score, and false-positive rate.

### `cross_vehicle_evaluation.py`
Provides the preliminary structure for same-vehicle and cross-vehicle evaluation. Same-vehicle testing will be used as the baseline, while cross-vehicle testing will evaluate how well the trained models perform on data from different vehicles.

### `requirements.txt`
Lists the Python libraries required to run the preliminary source code.

## Current Development Status

The source code in this folder represents the preliminary technical components of the proposed research. The complete experiment and final performance results will be produced after the selected multi-vehicle CAN bus dataset has been prepared and evaluated.
