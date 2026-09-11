# Evaluating the Cross-Vehicle Performance of Machine Learning-Based Intrusion Detection Models for Automotive CAN Bus Networks

## Course
IDB30102 - Research Methodology

## Group Information

**Group:** Group X

### Group Members
- Mohamad Syahmi Amrin Bin Mursham - 52215126522
- Muhammad Imran Zafri Bin Mohd Suhaini - 52215226113
- Muhammad Adam Danish Bin Mohd Anis - 52215125900
- Muhammad Muttakin Bin Mat Hussin - 52215226045

## Research Area
Automotive and Vehicle Security

## Research Problem
Many CAN bus intrusion detection studies report high performance, but most models are trained and tested using data from the same dataset or vehicle. This makes it difficult to know whether the models can maintain similar performance when they are tested using data from another vehicle.

Another issue is the lack of a consistent evaluation approach because previous studies use different datasets, preprocessing methods, and performance metrics.

## Research Aim
To evaluate the cross-vehicle performance of machine learning-based intrusion detection models for automotive CAN bus networks.

## Research Objectives
1. To identify suitable machine learning techniques and multi-vehicle CAN bus data for automotive intrusion detection.
2. To implement selected machine learning models for detecting normal and malicious CAN bus traffic.
3. To evaluate and compare the performance of the selected models across different vehicles using accuracy, precision, recall, F1-score, and false-positive rate.

   ## Research Objective Mapping

| Research Objective | Repository Evidence |
|---|---|
| Objective 1: Identify suitable machine learning techniques and multi-vehicle CAN bus data | `01_Research_Papers/`, `02_Literature_Review/`, `05_Data_or_Sample_Input/` |
| Objective 2: Implement selected machine learning models for detecting normal and malicious CAN bus traffic | `04_Source_Code/` |
| Objective 3: Evaluate and compare the selected models across different vehicles | `04_Source_Code/`, `06_Results_or_Expected_Output/` |

## Proposed Solution
This research will evaluate three machine learning models:
- Random Forest
- Decision Tree
- Support Vector Machine

The models will be tested using multi-vehicle CAN bus data under same-vehicle and cross-vehicle evaluation conditions.

## Research Methodology
Experimental Research Methodology

## Development Model
Not applicable. The study focuses on experimental evaluation and does not develop a complete software system.

## Proposed Dataset
can-train-and-test dataset

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- False-Positive Rate

  ## Evaluation Plan

The selected machine learning models will first be evaluated using a same-vehicle setting as the baseline. Each model will then undergo cross-vehicle evaluation, where training data from one vehicle is used and the model is tested using data from a different vehicle.

The can-train-and-test dataset will be used because it contains CAN bus data from multiple vehicles. Random Forest, Decision Tree, and Support Vector Machine will be evaluated under the same experimental conditions.

Performance will be compared using accuracy, precision, recall, F1-score, and false-positive rate (FPR). The comparison will be used to determine how well each model maintains its intrusion detection performance when applied to different vehicle data.

## Repository Structure

- `01_Research_Papers/` - Research papers and paper summaries
- `02_Literature_Review/` - Literature review supporting materials
- `03_Architecture_and_Flowchart/` - Proposed research architecture and flowchart
- `04_Source_Code/` - Preliminary machine learning and preprocessing code
- `05_Data_or_Sample_Input/` - Dataset information and sample input
- `06_Results_or_Expected_Output/` - Preliminary or expected outputs
- `07_References/` - References and external resources

## Tools and Technologies
- Python
- scikit-learn
- pandas
- NumPy
- Jupyter Notebook / VS Code
- GitHub

  ## Execution Instructions

### Requirements
The preliminary implementation requires Python 3 and the following libraries:

```bash
pip install pandas numpy scikit-learn
```

### Source Code
The preliminary Python scripts are available in the `04_Source_Code/` folder:

- `data_preprocessing.py` - Loads and prepares CAN bus data.
- `train_models.py` - Defines the Random Forest, Decision Tree, and Support Vector Machine models.
- `evaluation_metrics.py` - Calculates accuracy, precision, recall, F1-score, and false-positive rate.
- `cross_vehicle_evaluation.py` - Provides the same-vehicle and cross-vehicle evaluation structure.

### Running the Preliminary Code

Clone or download this repository and open the project directory.

Run the preliminary modules using:

```bash
python 04_Source_Code/data_preprocessing.py
python 04_Source_Code/train_models.py
python 04_Source_Code/evaluation_metrics.py
python 04_Source_Code/cross_vehicle_evaluation.py
```

The current source code represents the preliminary implementation. Full model training and experimental evaluation will be performed using the selected multi-vehicle CAN bus dataset.
