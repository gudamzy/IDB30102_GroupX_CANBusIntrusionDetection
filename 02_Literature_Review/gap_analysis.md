## Research Gap Analysis (Section 2.9)

| Gap | Evidence | How the Study Addresses It | Objective |
|---|---|---|---|
| **1. Limited cross-vehicle evaluation** | Many existing studies train and test their models using data from the same dataset or vehicle. Xiao et al. (2024) reported a performance decrease from 0.957 on Hyundai data to 0.615 on Chevrolet data, showing that strong performance on one vehicle may not generalise to another. | The selected models will first undergo same-vehicle evaluation as a baseline, followed by cross-vehicle evaluation using CAN bus data from different vehicles. | RO2, RO3 |
| **2. Inconsistent evaluation** | Previous studies use different datasets, preprocessing approaches, class distributions, labelling methods, and evaluation metrics. False-positive rate is also not consistently reported, making direct comparison difficult. | Random Forest, Decision Tree, and Support Vector Machine will be evaluated under the same experimental conditions using accuracy, precision, recall, F1-score, and false-positive rate. | RO3 |

## Traceability

**Problem Statement → Research Gap → Research Objective → Experimental Stage → Repository Location**

| Problem Statement | Gap | Objective | Experimental Stage | Repository Location |
|---|---|---|---|---|
| **1.3.1 Limited cross-vehicle evaluation** | Gap 1 | RO1, RO2, RO3 | Dataset preparation, model implementation, same-vehicle evaluation, and cross-vehicle evaluation | `01_Research_Papers/`, `02_Literature_Review/`, `04_Source_Code/`, `05_Data_or_Sample_Input/` |
| **1.3.2 Inconsistent evaluation** | Gap 2 | RO3 | Performance evaluation and comparison using consistent metrics | `04_Source_Code/`, `06_Results_or_Expected_Output/` |
