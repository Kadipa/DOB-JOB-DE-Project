# DOB-JOB-DE-Project
The Data Engineering ZoomCamp Project for NYC-DOB Job application filings dataset

# 🏗️ NYC DOB Job Data Pipeline (Batch ETL with AWS, dbt, Airflow, Metabase)

This project is a fully automated **batch data pipeline** that ingests, transforms, and visualizes NYC Department of Buildings (DOB) job application data.

It’s designed to simulate a real-world data engineering workflow using open-source tools and AWS services.

---

## 🔧 Tech Stack

| Stage                | Tool                             |
|---------------------|----------------------------------|
| Ingestion           | [DLT](https://github.com/airbytehq/dlt) (Python SDK) |
| Data Lake           | AWS S3                           |
| Cataloging          | AWS Glue                         |
| External Querying   | Redshift Spectrum                |
| Transformation      | dbt                              |
| Orchestration       | Apache Airflow                   |
| Visualization       | Metabase                         |
| Infra Provisioning  | Terraform                        |

---

## 🗺️ Architecture

