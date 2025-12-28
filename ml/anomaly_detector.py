# ml/anomaly_detector.py

import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(df):
    model = IsolationForest(
        n_estimators=100,
        contamination=0.2,
        random_state=42
    )

    model.fit(df[["level_num"]])
    df["anomaly"] = model.predict(df[["level_num"]])

    return df


if __name__ == "__main__":
    input_csv = "data/processed/parsed_logs.csv"
    output_csv = "data/anomalies/detected_anomalies.csv"

    df = pd.read_csv(input_csv)

    # Encode severity
    df["level_num"] = df["level"].map({
        "INFO": 0,
        "WARNING": 1,
        "ERROR": 2
    })

    result = detect_anomalies(df)

    # Save anomalies
    result.to_csv(output_csv, index=False)

    print("Anomaly detection completed!")
    print(result)
