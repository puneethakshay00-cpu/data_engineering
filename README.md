# Weather Data Engineering Pipeline

## Overview

This project implements an end-to-end data engineering pipeline that extracts weather data from the Weatherstack API, stores it in PostgreSQL, transforms it using dbt, orchestrates workflows with Apache Airflow, and visualizes analytics using Apache Superset.

The entire platform is containerized using Docker and Docker Compose.

---

## Architecture

```text
Weatherstack API
        │
        ▼
Apache Airflow
        │
        ▼
PostgreSQL (Raw Layer)
        │
        ▼
dev.raw_weather_data
        │
        ▼
dbt Staging Layer
        │
        ▼
dev.stg_weather_data
        │
        ▼
dbt Mart Layer
      ┌──────────────┐
      ▼              ▼
dev.daily_average   dev.weather_report
      │              │
      └──────┬───────┘
             ▼
Apache Superset Dashboard
```

---

## Technology Stack

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

### 1. Data Extraction

Airflow orchestrates the ingestion process and triggers Python scripts that fetch weather information from the Weatherstack API.

### 2. Data Loading

The extracted weather data is stored in PostgreSQL.

Raw table:

```sql
dev.raw_weather_data
```

### 3. Data Transformation

dbt transforms raw weather records into analytics-ready datasets.

#### Staging Layer

```sql
dev.stg_weather_data
```

#### Mart Layer

```sql
dev.daily_average
dev.weather_report
```

### 4. Visualization

Apache Superset connects to PostgreSQL and visualizes transformed weather metrics through interactive dashboards.

---

## Repository Structure

```text
.
├── airflow/
│   └── dags/
│       └── orchestrator.py
│
├── api-request/
│   ├── api_request.py
│   └── insert.py
│
├── dbt/
│   └── my_project/
│       ├── models/
│       │   ├── staging/
│       │   ├── mart/
│       │   └── sources/
│       └── dbt_project.yml
│
├── postgres/
│   ├── airflow_init.sql
│   └── superset_init.sql
│
├── docker/
│
├── docker-compose.yaml
└── README.md
```

---

## Data Models

### Raw Layer

```sql
dev.raw_weather_data
```

Stores weather data directly ingested from the API.

### Staging Layer

```sql
dev.stg_weather_data
```

Performs initial cleaning and standardization.

### Analytics Layer

```sql
dev.daily_average
```

Provides aggregated daily weather metrics.

```sql
dev.weather_report
```

Provides reporting-ready weather summaries.

---

## Skills Demonstrated

* Data Engineering
* ETL / ELT Pipeline Development
* Apache Airflow Workflow Orchestration
* PostgreSQL Data Warehousing
* dbt Data Modeling
* SQL Transformations
* Docker Containerization
* Dashboard Development with Superset

---

## Challenges Solved

During development the following issues were resolved:

* Docker Compose configuration issues
* PostgreSQL authentication and role management
* Superset initialization failures
* Multi-container networking
* Environment variable management
* dbt schema and model configuration
* Database connectivity across services

---

## Future Improvements

* Deploy to AWS/GCP
* Add CI/CD using GitHub Actions
* Add dbt tests and data quality checks
* Implement real-time weather streaming
* Add alerting and monitoring
* Create advanced analytical dashboards

```
```
