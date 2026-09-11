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
