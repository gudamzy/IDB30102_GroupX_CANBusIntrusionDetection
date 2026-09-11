## Evaluation Metrics Identified from Previous Research

| Metric | Use in Previous Research | Issue Identified | Used in This Study |
|---|---|---|---|
| **Accuracy** | Commonly reported in CAN bus intrusion detection studies | Accuracy alone may not provide a complete view of detection performance, especially when class distributions are imbalanced | Yes |
| **Precision** | Commonly used to evaluate intrusion detection performance | Should be considered together with other metrics for a more complete evaluation | Yes |
| **Recall** | Commonly used to measure the ability to detect malicious traffic | Important for identifying how many actual attacks are successfully detected | Yes |
| **F1-score** | Frequently reported together with precision and recall | Provides a balanced measure of precision and recall | Yes |
| **False-positive rate (FPR)** | Reported less consistently across previous studies | Limited reporting makes it difficult to compare how often normal CAN traffic is incorrectly classified as malicious | Yes |

## Metrics Selected for This Study

The performance of Random Forest, Decision Tree, and Support Vector Machine will be evaluated using the same set of metrics:

- Accuracy
- Precision
- Recall
- F1-score
- False-positive rate

These metrics will be applied to both same-vehicle and cross-vehicle evaluations. Using the same evaluation metrics for all three models allows their performance to be compared under consistent experimental conditions.

False-positive rate will be calculated as:

**FPR = FP / (FP + TN)**

where **FP** represents false positives and **TN** represents true negatives.

The preliminary implementation of the evaluation metrics is available in:

`04_Source_Code/evaluation_metrics.py`
