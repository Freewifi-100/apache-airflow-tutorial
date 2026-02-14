from airflow.sdk import dag, task, asset
from pendulum import datetime
import os

@asset(
    name="fetch_data",
    schedule="@daily",
    # schedule= "@once",
    uri="/opt/airflow/logs/data/data_extract.txt", # where the asset is stored (dependency link to)
)

def fetch_data(self):
    print("Fetching data...")
    # Ensure the directory exists
    os.makedirs(os.path.dirname(self.uri), exist_ok=True)

    # write the content to the file
    with open(self.uri, 'w') as f:
        f.write(f"Data extracted successfully !!!\n")
    print(f"Data written to {self.uri}")
