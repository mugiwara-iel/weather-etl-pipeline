import logging
import os
import pandas as pd
from google.cloud import bigquery

def load_to_bigquery(df: pd.DataFrame) -> None:
    project_id = os.getenv("GCP_PROJECT_ID")
    dataset_id = os.getenv("BQ_DATASET")
    table_id = os.getenv("BQ_TABLE")
    full_table_id = f"{project_id}.{dataset_id}.{table_id}"

    client = bigquery.Client(project=project_id)

    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=True,
    )

    job = client.load_table_from_dataframe(df, full_table_id, job_config=job_config)
    job.result()  # Wait for the load job to complete

    logging.info(f"Successfully loaded {len(df)} rows into {full_table_id}.")
