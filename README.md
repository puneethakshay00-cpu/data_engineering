# Weather Data Engineering Pipeline

## Project Overview

This project is an end-to-end data engineering pipeline that extracts weather data from the Weatherstack API, orchestrates workflows using Apache Airflow, stores data in PostgreSQL, transforms data using dbt, and visualizes insights through Apache Superset dashboards.

The entire platform is containerized using Docker and Docker Compose for easy deployment and reproducibility.

---

## Architecture

```text
Weatherstack API
        │
        ▼
 Apache Airflow
        │
        ▼
 PostgreSQL
        │
        ▼
      dbt
        │
        ▼
 Apache Superset
```

---

## Tech Stack

* Python
* Apache Airflow
* PostgreSQL
* dbt (Data Build Tool)
* Apache Superset
* Docker & Docker Compose
* Redis
* SQL

---

## Project Workflow

### Step 1: Data Extraction

Apache Airflow triggers a DAG that fetches weather data from the Weatherstack API.

### Step 2: Data Loading

The retrieved weather data is stored in PostgreSQL in the raw layer.

Example:

```sql
SELECT * FROM dev.raw_weather_data;
```

### Step 3: Data Transformation

dbt transforms raw weather records into analytics-ready tables.

Models used:

* stg_weather_data
* daily_average
* weather_report

### Step 4: Data Visualization

Apache Superset connects to PostgreSQL and creates dashboards and visualizations from transformed data.

---

## Features

* Automated weather data ingestion
* Workflow orchestration using Airflow
* PostgreSQL data warehouse
* SQL-based transformations with dbt
* Interactive dashboards using Superset
* Fully containerized environment

---

## Project Structure

```text
weather-data-project/
│
├── airflow/
│   └── dags/
│
├── api-request/
│
├── postgres/
│
├── dbt/
│
├── docker/
│
├── docker-compose.yaml
│
└── README.md
```

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/puneethakshay00-cpu/data_engineering_project_1.git
cd data_engineering_project_1
```

Start all services:

```bash
docker-compose up -d
```

Access services:

| Service    | URL                   |
| ---------- | --------------------- |
| Airflow    | http://localhost:8000 |
| Superset   | http://localhost:8088 |
| PostgreSQL | localhost:5000        |

---

## Sample Data Flow

```text
Weather API
    ↓
Airflow DAG
    ↓
PostgreSQL Raw Table
    ↓
dbt Models
    ↓
Analytics Tables
    ↓
Superset Dashboard
```

---

## Skills Demonstrated

* Data Engineering
* ETL/ELT Pipeline Development
* Workflow Orchestration
* SQL Data Modeling
* Docker Containerization
* Dashboard Development
* PostgreSQL Administration
* Data Transformation with dbt

---

## Challenges Solved

* Docker Compose configuration issues
* PostgreSQL authentication and role management
* Superset initialization and database connectivity
* Multi-container networking
* Environment variable management
* dbt integration with PostgreSQL

---

## Future Improvements

* Deploy on AWS/GCP
* Add CI/CD using GitHub Actions
* Implement data quality tests using dbt tests
* Add real-time weather streaming
* Build advanced dashboards and alerts
