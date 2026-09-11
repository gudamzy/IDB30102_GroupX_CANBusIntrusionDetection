import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(file_path):
    """Load CAN bus dataset from a CSV file."""
    data = pd.read_csv(file_path)

    print("Dataset loaded successfully.")
    print("Number of records:", len(data))
    print("Columns:", list(data.columns))

    return data


def check_missing_values(data):
    """Check for missing values in the dataset."""
    print("\nMissing values:")
    print(data.isnull().sum())


def remove_missing_values(data):
    """Remove records containing missing values."""
    return data.dropna()


def scale_features(data, feature_columns):
    """Scale selected numerical features."""
    scaler = StandardScaler()

    data[feature_columns] = scaler.fit_transform(
        data[feature_columns]
    )

    return data


if __name__ == "__main__":
    print("CAN Bus Intrusion Detection - Data Preprocessing")
    print("Preliminary preprocessing module ready.")
