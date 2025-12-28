# scripts/run_pipeline.py

from ingestion.log_collector import read_logs, parse_log
from ingestion.s3_uploader import upload_to_s3
from ml.feature_engineering import extract_features
from ml.anomaly_detector import detect_anomalies
from alerts.alert_system import send_alert
import pandas as pd

RAW_LOG_PATH = "data/raw/sample_logs.log"
PARSED_CSV = "data/processed/parsed_logs.csv"
ANOMALY_CSV = "data/anomalies/detected_anomalies.csv"


def run_pipeline():
    print("🚀 Starting Log Monitoring Pipeline...\n")

    # 1. Upload logs to S3
    upload_to_s3(RAW_LOG_PATH)

    # 2. Read & parse logs
    logs = read_logs(RAW_LOG_PATH)
    parsed = [parse_log(log) for log in logs]
    df = pd.DataFrame(parsed)
    df.to_csv(PARSED_CSV, index=False)

    # 3. Encode severity
    df["level_num"] = df["level"].map({
        "INFO": 0,
        "WARNING": 1,
        "ERROR": 2
    })

    # 4. Detect anomalies
    result = detect_anomalies(df)
    result.to_csv(ANOMALY_CSV, index=False)

    # 5. Trigger alerts
    anomalies = result[result["anomaly"] == -1]
    if anomalies.empty:
        print("✅ No anomalies detected.")
    else:
        print("\n🚨 Anomalies Detected:")
        for _, row in anomalies.iterrows():
            send_alert(row)

    print("\n✅ Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
