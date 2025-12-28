# ml/feature_engineering.py

import pandas as pd

def extract_features(csv_path):
    df = pd.read_csv(csv_path)

    features = {
        "total_logs": len(df),
        "info_count": (df["level"] == "INFO").sum(),
        "warning_count": (df["level"] == "WARNING").sum(),
        "error_count": (df["level"] == "ERROR").sum(),
    }

    return pd.DataFrame([features])


if __name__ == "__main__":
    input_csv = "data/processed/parsed_logs.csv"
    feature_df = extract_features(input_csv)

    print("Extracted Features:")
    print(feature_df)
