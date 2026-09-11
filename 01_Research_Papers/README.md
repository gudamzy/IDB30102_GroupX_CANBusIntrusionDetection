01_Research_Papers
Information on the papers cited in Chapter 2 of the proposal. PDFs are not uploaded because most are copyrighted;
each entry gives the DOI. Full APA references are in `07_References/references.md`.
---

X. Classification of normal and malicious traffic based on an ensemble of machine learning for a vehicle CAN-network
Author(s): Alalwany, E., & Mahgoub, I.
Year: 2022 · DOI: https://doi.org/10.3390/s22239195
Research problem: Which machine learning algorithms best separate normal and malicious CAN traffic?
Method / technique: Eight supervised algorithms and ensemble classifiers, including Random Forest, XGBoost and KNN.
Dataset / tools: Normal and malicious vehicle CAN-network traffic.
Main findings: Random Forest and XGBoost outperformed KNN in precision, recall and F-score; ensembles improved detection.
Limitation: Unbalanced data affected some models; known attacks only.
Relevance: Supports Random Forest as one of the three models compared.
2. Intrusion detection in vehicle CAN bus using machine learning: A comparative performance study
Author(s): Bari, B. S., Yelamarthi, K., & Ghafoor, S.
Year: 2023 · DOI: https://doi.org/10.3390/s23073610
Research problem: Compare classical ML classifiers for CAN intrusion detection on real vehicles.
Method / technique: SVM, Decision Tree, KNN on 15 frame features.
Dataset / tools: Kia Soul (461,341 samples) and Chevrolet Spark (313,930 samples); Python.
Main findings: Decision Tree best: 99.4% and 99.9%.
Limitation: Known attacks only; each vehicle evaluated separately.
Relevance: Supports Decision Tree as one of the three models; example of results reported per vehicle rather than across vehicles.
3. On the performance of detecting injection of fabricated messages into the CAN bus
Author(s): Ben Othmane, L., Dhulipala, L., Abdelkhalek, M., Multari, N., & Govindarasu, M.
Year: 2022 · DOI: https://doi.org/10.1109/TDSC.2020.2990192
Research problem: How well do detectors work on a moving vehicle rather than offline data?
Method / technique: Pearson correlation, k-means and HMM on speed/RPM; compared with two commercial IDS.
Dataset / tools: Moving 2017 Ford Transit via Raspberry Pi + PiCAN.
Main findings: k-means detects 71–79% of attacks with 45–68% false positives; HMM 42.5% false positives.
Limitation: Two injected signals only.
Relevance: Evidence that real-vehicle testing gives lower results and that false-positive rate matters (Section 2.7).
4. TCAN-IDS: Intrusion detection system for Internet of Vehicle using temporal convolutional attention network
Author(s): Cheng, P., Xu, K., Li, S., & Han, M.
Year: 2022 · DOI: https://doi.org/10.3390/sym14020310
Research problem: Capture temporal structure of CAN traffic.
Method / technique: Channel and spatial attention over 64-message windows.
Dataset / tools: HCRL Signal Extraction dataset.
Main findings: F1 99.92–99.98%; 3.4 ms per message.
Limitation: Window-level labelling inflates results; F1 misdefined (Eq. 13).
Relevance: Example of window-based evaluation that is not directly comparable (Problem Statement 1.3.2).
5. An efficient intrusion detection system in IoV using improved random forest model
Author(s): Dasari, D. R., & Gottumukkala, H.
Year: 2024 · DOI: https://doi.org/10.18280/ijtdi.080412
Research problem: Efficient detection for Internet of Vehicles traffic.
Method / technique: Improved Random Forest with SMOTEBoost and feature importance selection.
Dataset / tools: CICIDS-2018.
Main findings: 0.99 accuracy, 1.1 ms inference, 240 MB memory.
Limitation: Dataset contains no CAN traffic.
Relevance: Shows strong Random Forest results, but on network traffic, not CAN data.
6. can-train-and-test: A curated CAN dataset for automotive intrusion detection
Author(s): Lampe, B., & Meng, W.
Year: 2024 · DOI: https://doi.org/10.1016/j.cose.2024.103777 (preprint: arXiv 2308.04972)
Research problem: Public CAN datasets cover one vehicle and few attacks, so IDS generalisation cannot be measured.
Method / technique: Captured traffic from four vehicles, labelled every frame, curated four train/test sub-datasets; benchmarked 18 ML IDS models.
Dataset / tools: 2011 Chevrolet Impala, 2011 Chevrolet Traverse, 2016 Chevrolet Silverado, 2017 Subaru Forester; Python, python-can, pandas.
Main findings: Provides known/unknown vehicle and known/unknown attack test subsets for every sub-dataset; nine attack types.
Limitation: Two manufacturers only; limited to the captured attack scenarios.
Relevance: Dataset used in this study; `test_01` is the same-vehicle test and `test_02` the cross-vehicle test. Their benchmark reports accuracy, precision, recall and F1-score but not FPR.
X. Detecting CAN bus attacks in autonomous vehicles using deep learning
Author(s): Siddiqui, H., Siddiqui, S. T., Kibriya, H., Rana, N., Khan, W. Z., & Tahir, A.
Year: 2025 · DOI: https://doi.org/10.1109/ICETECC65365.2025.11070252
Research problem: Detect DoS, fuzzy, gear and RPM spoofing attacks on the CAN bus.
Method / technique: 1D convolutional layer with stacked bidirectional LSTM layers.
Dataset / tools: HCRL Car-Hacking dataset.
Main findings: About 99.5% accuracy, precision, recall and F1-score.
Limitation: One dataset from one vehicle.
Relevance: Source for the CAN attack classes described in Sections 1.1 and 2.2; example of single-dataset evaluation.
X. ConvIDS: A convolutional LSTM based intrusion detection model for in-vehicle CAN bus
Author(s): Wu, S., Li, S., & Sun, W.
Year: 2023 · DOI: https://doi.org/10.1109/AUTEEE60196.2023.10408040
Research problem: Capture temporal patterns in CAN traffic for detection.
Method / technique: One-hot encoded CAN IDs stacked into images and classified with a multi-layer ConvLSTM.
Dataset / tools: Hyundai Sonata CAN traffic (stationary).
Main findings: About 99.95% accuracy.
Limitation: One vehicle; deep model is more complex than classical ML.
Relevance: Example of deep learning in Section 2.4; supports choosing classical models for a controlled comparison.
9. A novel feature extraction framework using graph node attention network for in-vehicle networks intrusion detection
Author(s): Xiao, J., Chen, H., & Zhong, F.
Year: 2024 · DOI: https://doi.org/10.1109/JSYST.2023.3337091
Research problem: Window-level IDS cannot locate the malicious frame.
Method / technique: Converts traffic windows to graphs; graph node attention network with Random Forest; per-ID detection.
Dataset / tools: HCRL Car-Hacking and Survival Analysis datasets; PyTorch on a laptop.
Main findings: Accuracy 0.957 on Hyundai traffic but 0.615 on Chevrolet traffic; 31–38 ms detection time.
Limitation: Laptop hardware, not automotive; normal frames sharing a flagged ID are also filtered.
Relevance: Main evidence for Problem Statement 1.3.1 (limited cross-vehicle evaluation).
10. An effective in-vehicle CAN bus intrusion detection system using CNN deep learning approach
Author(s): Hossain, M. D., Inoue, H., Ochiai, H., Fall, D., & Kadobayashi, Y.
Year: 2020 · DOI: https://doi.org/10.1109/GLOBECOM42002.2020.9322395
Research problem: Detect DoS, fuzzing and spoofing on CAN without decoding messages.
Method / technique: 1D CNN on raw ID, DLC and payload bytes.
Dataset / tools: NAIST data from three cars (Toyota, Subaru, Suzuki).
Main findings: Around 99.99% accuracy.
Limitation: Each car tested separately; no test on a car not used in training.
Relevance: Table 2.1; evidence for limited cross-vehicle evaluation.
11. Transformer-based attention network for in-vehicle intrusion detection
Author(s): Nguyen, T. P., Nam, H., & Kim, D.
Year: 2023 · DOI: https://doi.org/10.1109/ACCESS.2023.3282110
Research problem: Model long-range dependencies in CAN ID sequences.
Method / technique: Self-attention (transformer) on sequences of CAN IDs.
Dataset / tools: Three HCRL datasets; GPU workstation.
Main findings: High detection, at about five times the computation of a CNN-LSTM baseline.
Limitation: Speed measured on a workstation, not in-vehicle hardware.
Relevance: Table 2.1; supports using simpler classical models for a controlled comparison.
12. A hybrid intrusion detection model based on dynamic spatial-temporal graph neural network
Author(s): Zhang, J., Fan, X., & Zhao, Z.
Year: 2025 · DOI: https://doi.org/10.1038/s41598-025-18401-3
Research problem: Model spatial and temporal CAN relationships.
Method / technique: Graph neural network (GCN-2-Former).
Dataset / tools: Car-Hacking, CICIDS2017.
Main findings: 100% on Car-Hacking.
Limitation: Graph-level labels; FPR formula misdefined.
Relevance: Table 2.1; evidence for inconsistent evaluation (Problem Statement 1.3.2).
13. A stacked machine learning-based IDS for internal and external networks in smart connected vehicles
Author(s): Zhou, X., Wu, Y., Lin, J., Xu, Y., & Woo, S.
Year: 2025 · DOI: https://doi.org/10.3390/sym17060874
Research problem: Detect attacks on in-vehicle and external networks.
Method / technique: Stacked machine learning ensemble.
Dataset / tools: Simulated CAN data (CANoe, VAE-augmented), CICIDS2017; Raspberry Pi 3B+.
Main findings: 99.99% in testing; recall 91.95% on Raspberry Pi.
Limitation: Mostly synthetic data.
Relevance: Table 2.1; shows results can drop outside the lab setting.
