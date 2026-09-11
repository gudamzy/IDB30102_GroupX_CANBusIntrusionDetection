## Comparison of Existing Techniques

| Family | Examples | Reported Results | Why (Not) Chosen |
|---|---|---|---|
| Decision Tree | Bari et al. (2023) | 99.4–99.9% on Kia Soul / Chevrolet Spark | Chosen – simple, fast, and strong on known attacks |
| Random Forest | Alalwany & Mahgoub (2022); Dasari & Gottumukkala (2024) | Among the best classical models; ~0.99 | Chosen – consistently strong in the reviewed studies |
| Support Vector Machine | Bari et al. (2023) compared SVM with DT and KNN | Lower than DT in Bari et al. | Chosen – provides a different decision boundary from tree-based models |
| KNN | Alalwany & Mahgoub (2022) | Outperformed by RF and XGBoost | Not chosen – prediction can be slower on large datasets |
| Deep Learning (ConvLSTM, CNN-BiLSTM, attention) | Wu et al. (2023); Siddiqui et al. (2025); Cheng et al. (2022) | 99.5–99.98% | Not chosen – more complex; this study focuses on comparing selected ML models under the same experimental conditions rather than developing a new architecture |

The three selected models will be evaluated using the same data preparation and experimental conditions so that their same-vehicle and cross-vehicle performance can be compared fairly.
