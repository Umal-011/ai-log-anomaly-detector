# ingestion/s3_uploader.py

import boto3

BUCKET_NAME = "s3-bucket-uma-2025"
S3_KEY = "logs/sample_logs.log"


def upload_to_s3(file_path):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, BUCKET_NAME, S3_KEY)
    print("✅ Logs uploaded to S3 successfully!")


if __name__ == "__main__":
    upload_to_s3("data/raw/sample_logs.log")
