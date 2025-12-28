# alerts/alert_system.py

import pandas as pd


def send_alert(log):
    print("🚨 ALERT TRIGGERED 🚨")
    print(f"Time: {log['timestamp']}")
    print(f"Level: {log['level']}")
    print(f"Message: {log['message']}")
    print("-" * 40)


if __name__ == "__main__":
    anomaly_csv = "data/anomalies/detected_anomalies.csv"
    df = pd.read_csv(anomaly_csv)

    anomalies = df[df["anomaly"] == -1]

    if anomalies.empty:
        print("No anomalies detected.")
    else:
        for _, row in anomalies.iterrows():
            send_alert(row)
