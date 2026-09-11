Research gap analysis (Section 2.9)
Gap	Evidence	How the study addresses it	Objective
1. Limited cross-vehicle evaluation	Most studies train and test on the same dataset or vehicle; Xiao et al. (2024) 0.957 → 0.615. Lampe & Meng (2024) benchmarked 18 models across vehicles but did not report FPR	Train on `train_01`, test on `test_01` (same vehicle) and `test_02` (different vehicle) for four sub-datasets	RO2, RO3
2. Inconsistent evaluation	Different datasets, preprocessing, class balancing, labelling and metrics; FPR often missing (Ben Othmane et al., 2022, show why it matters)	Same features, same training sample, per-message labels, five metrics including FPR for every model	RO3
Traceability
Problem statement → gap → objective → stage → repository location
Problem statement	Gap	Objective	Stage (Section 3.2.5)	Location
1.3.1 Limited cross-vehicle evaluation	1	RO1, RO2, RO3	Stages 1, 3, 4, 5	`05_Data_or_Sample_Input/`, `04_Source_Code/canids/experiment.py`
1.3.2 Inconsistent evaluation	2	RO3	Stages 2, 6	`04_Source_Code/canids/features.py`, `metrics.py`
