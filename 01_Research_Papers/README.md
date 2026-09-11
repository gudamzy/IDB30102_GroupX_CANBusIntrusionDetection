# 01_Research_Papers

Information on the papers cited in Chapter 2 of the proposal. PDFs are not uploaded because most are copyrighted; each entry gives the DOI. Full APA references are available in `07_References/references.md`.

---

## 1. Classification of Normal and Malicious Traffic Based on an Ensemble of Machine Learning for a Vehicle CAN-Network

**Author(s):** Alalwany, E., & Mahgoub, I.
**Year:** 2022
**DOI:** https://doi.org/10.3390/s22239195

**Research problem:** Which machine learning algorithms best separate normal and malicious CAN traffic?

**Method / technique:** Eight supervised algorithms and ensemble classifiers, including Random Forest, XGBoost, and KNN.

**Dataset / tools:** Normal and malicious vehicle CAN-network traffic.

**Main findings:** Random Forest and XGBoost outperformed KNN in precision, recall, and F-score; ensemble methods improved detection performance.

**Limitation:** Unbalanced data affected some models, and only known attacks were evaluated.

**Relevance:** Supports Random Forest as one of the three models compared in this study.

---

## 2. Intrusion Detection in Vehicle CAN Bus Using Machine Learning: A Comparative Performance Study

**Author(s):** Bari, B. S., Yelamarthi, K., & Ghafoor, S.
**Year:** 2023
**DOI:** https://doi.org/10.3390/s23073610

**Research problem:** Compare classical machine learning classifiers for CAN intrusion detection on real vehicles.

**Method / technique:** SVM, Decision Tree, and KNN using 15 frame features.

**Dataset / tools:** Kia Soul (461,341 samples) and Chevrolet Spark (313,930 samples); Python.

**Main findings:** Decision Tree achieved the best performance, with accuracy of 99.4% and 99.9%.

**Limitation:** Only known attacks were evaluated, and each vehicle was evaluated separately.

**Relevance:** Supports Decision Tree as one of the three models and provides an example of results being reported per vehicle rather than across vehicles.

---

## 3. On the Performance of Detecting Injection of Fabricated Messages into the CAN Bus

**Author(s):** Ben Othmane, L., Dhulipala, L., Abdelkhalek, M., Multari, N., & Govindarasu, M.
**Year:** 2022
**DOI:** https://doi.org/10.1109/TDSC.2020.2990192

**Research problem:** How well do intrusion detectors perform on a moving vehicle rather than only on offline data?

**Method / technique:** Pearson correlation, k-means, and HMM on speed and RPM; compared with two commercial IDS solutions.

**Dataset / tools:** Moving 2017 Ford Transit using Raspberry Pi and PiCAN.

**Main findings:** k-means detected 71–79% of attacks with 45–68% false positives, while HMM produced a 42.5% false-positive rate.

**Limitation:** Only two injected signals were evaluated.

**Relevance:** Provides evidence that real-vehicle testing can produce lower detection performance and demonstrates the importance of considering the false-positive rate (Section 2.7).

---

## 4. TCAN-IDS: Intrusion Detection System for Internet of Vehicle Using Temporal Convolutional Attention Network

**Author(s):** Cheng, P., Xu, K., Li, S., & Han, M.
**Year:** 2022
**DOI:** https://doi.org/10.3390/sym14020310

**Research problem:** Capture the temporal structure of CAN traffic for intrusion detection.

**Method / technique:** Channel and spatial attention over 64-message windows.

**Dataset / tools:** HCRL Signal Extraction dataset.

**Main findings:** Achieved F1-scores between 99.92% and 99.98%, with approximately 3.4 ms processing time per message.

**Limitation:** Window-level labelling may inflate the reported results, and the F1-score is misdefined in Equation 13.

**Relevance:** Provides an example of window-based evaluation that is not directly comparable with frame-level evaluation (Problem Statement 1.3.2).

---

## 5. An Efficient Intrusion Detection System in IoV Using Improved Random Forest Model

**Author(s):** Dasari, D. R., & Gottumukkala, H.
**Year:** 2024
**DOI:** https://doi.org/10.18280/ijtdi.080412

**Research problem:** Develop an efficient intrusion detection approach for Internet of Vehicles traffic.

**Method / technique:** Improved Random Forest using SMOTEBoost and feature importance selection.

**Dataset / tools:** CICIDS-2018.

**Main findings:** Achieved 0.99 accuracy, 1.1 ms inference time, and approximately 240 MB memory usage.

**Limitation:** The dataset does not contain CAN traffic.

**Relevance:** Demonstrates strong Random Forest performance but on conventional network traffic rather than CAN data.

---

## 6. can-train-and-test: A Curated CAN Dataset for Automotive Intrusion Detection

**Author(s):** Lampe, B., & Meng, W.
**Year:** 2024
**DOI:** https://doi.org/10.1016/j.cose.2024.103777
**Preprint:** arXiv 2308.04972

**Research problem:** Existing public CAN datasets commonly cover only one vehicle and a limited number of attacks, making IDS generalisation difficult to measure.

**Method / technique:** Captured traffic from four vehicles, labelled every frame, curated four train/test sub-datasets, and benchmarked 18 machine learning IDS models.

**Dataset / tools:** 2011 Chevrolet Impala, 2011 Chevrolet Traverse, 2016 Chevrolet Silverado, and 2017 Subaru Forester; Python, python-can, and pandas.

**Main findings:** Provides known/unknown vehicle and known/unknown attack test subsets for every sub-dataset, covering nine attack types.

**Limitation:** Only two vehicle manufacturers are represented, and evaluation is limited to the captured attack scenarios.

**Relevance:** This is the dataset used in the present study. `test_01` represents the same-vehicle test, while `test_02` represents the cross-vehicle test. The original benchmark reports accuracy, precision, recall, and F1-score but does not report FPR.

---

## 7. Detecting CAN Bus Attacks in Autonomous Vehicles Using Deep Learning

**Author(s):** Siddiqui, H., Siddiqui, S. T., Kibriya, H., Rana, N., Khan, W. Z., & Tahir, A.
**Year:** 2025
**DOI:** https://doi.org/10.1109/ICETECC65365.2025.11070252

**Research problem:** Detect DoS, fuzzy, gear, and RPM spoofing attacks on the CAN bus.

**Method / technique:** 1D convolutional layer with stacked bidirectional LSTM layers.

**Dataset / tools:** HCRL Car-Hacking dataset.

**Main findings:** Achieved approximately 99.5% accuracy, precision, recall, and F1-score.

**Limitation:** Evaluation was performed using one dataset from one vehicle.

**Relevance:** Provides a source for the CAN attack classes described in Sections 1.1 and 2.2 and serves as an example of single-dataset evaluation.

---

## 8. ConvIDS: A Convolutional LSTM Based Intrusion Detection Model for In-Vehicle CAN Bus

**Author(s):** Wu, S., Li, S., & Sun, W.
**Year:** 2023
**DOI:** https://doi.org/10.1109/AUTEEE60196.2023.10408040

**Research problem:** Capture temporal patterns in CAN traffic for intrusion detection.

**Method / technique:** One-hot encoded CAN IDs stacked into images and classified using a multi-layer ConvLSTM.

**Dataset / tools:** Hyundai Sonata CAN traffic collected while stationary.

**Main findings:** Achieved approximately 99.95% accuracy.

**Limitation:** Evaluation involved only one vehicle, and the deep learning model is more complex than classical machine learning approaches.

**Relevance:** Provides an example of deep learning for CAN intrusion detection in Section 2.4 and supports the selection of classical models for a controlled comparison.

---

## 9. A Novel Feature Extraction Framework Using Graph Node Attention Network for In-Vehicle Networks Intrusion Detection

**Author(s):** Xiao, J., Chen, H., & Zhong, F.
**Year:** 2024
**DOI:** https://doi.org/10.1109/JSYST.2023.3337091

**Research problem:** Window-level intrusion detection systems cannot precisely identify the malicious frame.

**Method / technique:** Converts traffic windows into graphs and applies a graph node attention network with Random Forest for per-ID detection.

**Dataset / tools:** HCRL Car-Hacking and Survival Analysis datasets; PyTorch running on a laptop.

**Main findings:** Achieved accuracy of 0.957 on Hyundai traffic but only 0.615 on Chevrolet traffic, with detection times of approximately 31–38 ms.

**Limitation:** Testing was conducted on laptop hardware rather than automotive hardware, and normal frames sharing a flagged CAN ID may also be filtered.

**Relevance:** Provides important evidence for Problem Statement 1.3.1 regarding limited cross-vehicle evaluation.

---

## 10. An Effective In-Vehicle CAN Bus Intrusion Detection System Using CNN Deep Learning Approach

**Author(s):** Hossain, M. D., Inoue, H., Ochiai, H., Fall, D., & Kadobayashi, Y.
**Year:** 2020
**DOI:** https://doi.org/10.1109/GLOBECOM42002.2020.9322395

**Research problem:** Detect DoS, fuzzing, and spoofing attacks on CAN without decoding CAN messages.

**Method / technique:** 1D CNN using raw CAN ID, DLC, and payload bytes.

**Dataset / tools:** NAIST data collected from three vehicles: Toyota, Subaru, and Suzuki.

**Main findings:** Achieved approximately 99.99% accuracy.

**Limitation:** Each vehicle was tested separately, with no evaluation on a vehicle that was not used during training.

**Relevance:** Included in Table 2.1 and provides evidence of limited cross-vehicle evaluation.

---

## 11. Transformer-Based Attention Network for In-Vehicle Intrusion Detection

**Author(s):** Nguyen, T. P., Nam, H., & Kim, D.
**Year:** 2023
**DOI:** https://doi.org/10.1109/ACCESS.2023.3282110

**Research problem:** Model long-range dependencies within CAN ID sequences.

**Method / technique:** Self-attention using a transformer architecture on sequences of CAN IDs.

**Dataset / tools:** Three HCRL datasets; GPU workstation.

**Main findings:** Achieved high detection performance but required approximately five times the computation of a CNN-LSTM baseline.

**Limitation:** Processing speed was measured using a workstation rather than actual in-vehicle hardware.

**Relevance:** Included in Table 2.1 and supports the use of simpler classical machine learning models for a controlled comparison.

---

## 12. A Hybrid Intrusion Detection Model Based on Dynamic Spatial-Temporal Graph Neural Network

**Author(s):** Zhang, J., Fan, X., & Zhao, Z.
**Year:** 2025
**DOI:** https://doi.org/10.1038/s41598-025-18401-3

**Research problem:** Model both spatial and temporal relationships within CAN traffic.

**Method / technique:** Graph neural network using the GCN-2-Former architecture.

**Dataset / tools:** Car-Hacking and CICIDS2017 datasets.

**Main findings:** Achieved 100% performance on the Car-Hacking dataset.

**Limitation:** Uses graph-level labels, and the FPR formula is misdefined.

**Relevance:** Included in Table 2.1 and provides evidence of inconsistent evaluation approaches (Problem Statement 1.3.2).

---

## 13. A Stacked Machine Learning-Based IDS for Internal and External Networks in Smart Connected Vehicles

**Author(s):** Zhou, X., Wu, Y., Lin, J., Xu, Y., & Woo, S.
**Year:** 2025
**DOI:** https://doi.org/10.3390/sym17060874

**Research problem:** Detect attacks affecting both in-vehicle and external networks in smart connected vehicles.

**Method / technique:** Stacked machine learning ensemble.

**Dataset / tools:** Simulated CAN data generated using CANoe and VAE augmentation, CICIDS2017, and Raspberry Pi 3B+.

**Main findings:** Achieved 99.99% performance during testing, while recall decreased to 91.95% when evaluated on Raspberry Pi.

**Limitation:** The evaluation relies mostly on synthetic data.

**Relevance:** Included in Table 2.1 and demonstrates that IDS performance can decrease when moving from laboratory evaluation to a more realistic deployment environment.
