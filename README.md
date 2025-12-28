# AI Log Anomaly Detector

The **AI Log Anomaly Detector** is an end-to-end pipeline that automates log monitoring, anomaly detection, and alerting.  
It leverages **machine learning** to identify unusual patterns in log data and integrates with **AWS services** for scalable storage and analysis.

---

## Features

- **Log Ingestion**: Collects application logs and uploads raw logs to AWS S3
- **Log Parsing**: Converts unstructured logs into structured data
- **Feature Engineering**: Extracts ML-ready numerical features
- **Anomaly Detection**: Detects abnormal log behavior using Isolation Forest
- **Alerting**: Triggers alerts when anomalies are detected
- **Storage**: Persists anomaly results in AWS DynamoDB

---

## Project Structure

ai-log-anomaly-detector/
│
├── ingestion/
│ ├── log_collector.py
│ └── s3_uploader.py
│
├── ml/
│ ├── feature_engineering.py
│ └── anomaly_detector.py
│
├── alerts/
│ └── alert_system.py
│
├── storage/
│ └── dynamodb_client.py
│
├── scripts/
│ └── run_pipeline.py
│
├── data/
│ ├── raw/
│ ├── processed/
│ └── anomalies/
│
├── requirements.txt
├── README.md
└── .gitignore

---

## How It Works

The entire system runs through **a single pipeline entry point**:

```bash
python -m scripts.run_pipeline
```

## Internally, the pipeline performs the following steps:

- Uploads raw logs to AWS S3
- Parses and processes logs using ETL
- Converts logs into ML-ready features
- Detects anomalies using Isolation Forest
- Stores anomaly results in DynamoDB
- Triggers alerts for detected anomalies

## Machine Learning Approach

Model: Isolation Forest

- Reason:
  Unsupervised anomaly detection
  Suitable for log-based data
  No labeled data required
- Features Used:
  Log severity encoding
  Frequency-based patterns

## Cloud Design Rationale

- AWS S3
  Scalable and cost-effective storage for raw logs
- AWS DynamoDB
  Fast NoSQL storage for processed anomaly results
- Why not store raw logs directly in DynamoDB?
  Logs are unstructured and high-volume
  DynamoDB is optimized for structured, query-ready data

## Key Learnings

- Log ingestion and parsing
- ETL pipeline design
- Feature engineering for ML
- Unsupervised anomaly detection
- AWS cloud integration
- Production-style pipeline orchestration

## Author

Uma Shankar Mannuru
B.Tech Artificial Intelligence Student
Skills: Python, AWS, Data Pipelines, Machine Learning
