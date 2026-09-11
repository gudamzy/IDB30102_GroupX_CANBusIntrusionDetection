from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC


def create_models():
    """Create the machine learning models used in the research."""

    models = {
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

        "Decision Tree": DecisionTreeClassifier(
            random_state=42
        ),

        "Support Vector Machine": SVC()
    }

    return models


def train_models(models, X_train, y_train):
    """Train all selected machine learning models."""

    trained_models = {}

    for name, model in models.items():
        print(f"Training {name}...")

        model.fit(X_train, y_train)
        trained_models[name] = model

    return trained_models


if __name__ == "__main__":
    models = create_models()

    print("Selected models:")
    for model_name in models:
        print("-", model_name)
