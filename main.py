import logging
from dotenv import load_dotenv
from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.load import load_to_bigquery

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def run_pipeline():
    load_dotenv()
    logging.info("Starting Weather ETL Pipeline...")
    raw_data = extract_weather_data(location="Candelaria,Quezon")
    clean_df = transform_weather_data(raw_data, city="Candelaria")
    load_to_bigquery(clean_df)
    logging.info("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
