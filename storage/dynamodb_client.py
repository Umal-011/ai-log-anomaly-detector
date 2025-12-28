# storage/dynamodb_client.py

import boto3
import pandas as pd
import uuid

TABLE_NAME = "LogAnomalies"


def save_anomalies(csv_path):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE_NAME)

    df = pd.read_csv(csv_path)
    anomalies = df[df["anomaly"] == -1]

    if anomalies.empty:
        print("No anomalies to store.")
        return

    for _, row in anomalies.iterrows():
        table.put_item(
            Item={
                "log_id": str(uuid.uuid4()),
                "timestamp": row["timestamp"],
                "level": row["level"],
                "message": row["message"]
            }
        )

    print("✅ Anomalies saved to DynamoDB successfully!")


if __name__ == "__main__":
    save_anomalies("data/anomalies/detected_anomalies.csv")
