# Automated Weather ETL Pipeline

![Daily Weather ETL Pipeline](https://github.com)

An end-to-end, automated Python ETL (Extract, Transform, Load) pipeline that fetches daily weather forecast data from a public REST API, cleans and validates nested JSON structures using Pandas, and loads structured tables into **Google BigQuery** on a daily schedule via **GitHub Actions**.

## Architecture

```text
[wttr.in REST API] ──▶ [Python Extract] ──▶ [Pandas Transform & Validate] ──▶ [Google BigQuery]
                                                                                       ▲
                                                             [GitHub Actions Cron] ────┘
```

## Key Data Engineering Features

- **Modular ETL Design:** Separated into independent `extract.py`, `transform.py`, and `load.py` modules orchestrated by `main.py`.
- **Nested JSON Flattening & Schema Enforcement:** Parses multi-day nested hourly JSON arrays into normalized tabular records with explicit data types and UTC ingestion timestamps.
- **Data Quality & Idempotency:** Enforces null-value filtering, duplicate key removal, and `WRITE_TRUNCATE` load dispositions to keep warehouse tables clean across scheduled runs.
- **CI/CD Cloud Orchestration:** Scheduled via GitHub Actions (`cron: '0 0 * * *'`) using encrypted Repository Secrets for zero-hardcoded-credential security.
- **Structured Observability:** Implements centralized Python logging (`INFO`/`ERROR`) and HTTP exception handling to audit row counts and API status codes.

## Tech Stack

- **Language:** Python 3.11
- **Data Processing:** Pandas, Requests
- **Cloud Data Warehouse:** Google BigQuery
- **Orchestration & CI/CD:** GitHub Actions
- **Version Control & Config:** Git, `python-dotenv`

## Project Structure

```text
weather-etl-pipeline/
├── .github/workflows/
│   └── etl_schedule.yml    # Daily automated GitHub Actions workflow
├── src/
│   ├── extract.py          # REST API extraction with error handling
│   ├── transform.py        # Nested JSON parsing, cleaning & validation
│   └── load.py             # BigQuery client loader
├── main.py                 # Pipeline entry point & logging config
├── requirements.txt        # Pinned Python dependencies
└── .gitignore              # Excludes .env, venv/, and GCP service keys
```

## Local Setup & Execution

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd weather-etl-pipeline
   ```
2. Create and activate a virtual environment, then install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Configure environment variables in a `.env` file (`GCP_PROJECT_ID`, `BQ_DATASET`, `BQ_TABLE`, `GOOGLE_APPLICATION_CREDENTIALS`) and run:
   ```bash
   python3 main.py
   ```
