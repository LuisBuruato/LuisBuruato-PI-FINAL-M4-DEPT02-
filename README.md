# Data Pipeline - Proyecto Integrador

Arquitectura:

EC2
  └─ Docker
       └─ Apache Airflow

Pipeline:

Airbyte (ingestion)
     ↓
Spark (transform)
     ↓
Gold Layer (Parquet)

Orquestación:
Apache Airflow DAG

CI/CD:
GitHub Actions