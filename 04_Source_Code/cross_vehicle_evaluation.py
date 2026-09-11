from train_models import create_models, train_models
from evaluation_metrics import evaluate_model


def run_same_vehicle_evaluation(X_train, X_test, y_train, y_test):
    """
    Train and test the models using data from the same vehicle.
    This will be used as the baseline evaluation.
    """

    models = create_models()
    trained_models = train_models(models, X_train, y_train)

    results = {}

    for name, model in trained_models.items():
        predictions = model.predict(X_test)
        results[name] = evaluate_model(y_test, predictions)

    return results


def run_cross_vehicle_evaluation(
    X_train_vehicle,
    y_train_vehicle,
    X_test_vehicle,
    y_test_vehicle
):
    """
    Train the models using data from one vehicle
    and test them using data from another vehicle.
    """

    models = create_models()
    trained_models = train_models(
        models,
        X_train_vehicle,
        y_train_vehicle
    )

    results = {}

    for name, model in trained_models.items():
        predictions = model.predict(X_test_vehicle)

        results[name] = evaluate_model(
            y_test_vehicle,
            predictions
        )

    return results


if __name__ == "__main__":
    print("Cross-vehicle evaluation module ready.")
    print("Baseline: same-vehicle evaluation")
    print("Main experiment: cross-vehicle evaluation")
