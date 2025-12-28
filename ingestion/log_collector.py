# ingestion/log_collector.py

import pandas as pd


def read_logs(file_path):
    logs = []
    with open(file_path, "r") as file:
        for line in file:
            logs.append(line.strip())
    return logs


def parse_log(log_line):
    parts = log_line.split(" ", 3)
    return {
        "timestamp": parts[0] + " " + parts[1],
        "level": parts[2],
        "message": parts[3]
    }


if __name__ == "__main__":
    log_file_path = "data/raw/sample_logs.log"
    raw_logs = read_logs(log_file_path)

    parsed_logs = [parse_log(log) for log in raw_logs]

    # Convert to DataFrame
    df = pd.DataFrame(parsed_logs)

    # Save processed data
    output_path = "data/processed/parsed_logs.csv"
    df.to_csv(output_path, index=False)

    print("Parsed logs saved successfully!")
    print(df)
