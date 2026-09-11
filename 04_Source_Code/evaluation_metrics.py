from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


def calculate_false_positive_rate(y_true, y_pred):
    """Calculate false-positive rate from confusion matrix."""

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

    fpr = fp / (fp + tn)

    return fpr


def evaluate_model(y_true, y_pred):
    """Calculate the main evaluation metrics used in the research."""

    results = {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall": recall_score(y_true, y_pred, zero_division=0),
        "F1-score": f1_score(y_true, y_pred, zero_division=0),
        "False-Positive Rate": calculate_false_positive_rate(
            y_true,
            y_pred
        )
    }

    return results


if __name__ == "__main__":
    print("Evaluation metrics module ready.")
