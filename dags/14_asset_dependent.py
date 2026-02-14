from airflow.sdk import dag, task, asset
from pendulum import datetime
import os
from asset_13 import fetch_data

@asset(
    name="processed_data",
    schedule=fetch_data, # inherit schedule from fetch_data asset
    uri="/opt/airflow/logs/data/data_processed.txt", # where the asset is stored (dependency link to)
    is_paused_upon_creation=True, # start in paused state until the dependency is met
)

def process_data(self):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(self.uri), exist_ok=True)

    # write the content to the file
    with open(self.uri, 'w') as f:
        f.write(f"Data processed successfully!\n")

    print(f"Data processed to {self.uri}")
