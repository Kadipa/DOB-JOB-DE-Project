# 🏙️ NYC DOB Job Data Pipeline — DE Zoomcamp 2025 Course Project

This project is part of the Data Engineering Zoomcamp course and follows the full project rubric. It builds a real-world batch data pipeline to ingest, transform, and visualize New York City Department of Buildings (DOB) job application filings using modern data engineering tools and AWS cloud services.

---

## 🎯 Problem Description

New York City’s Department of Buildings publishes building job application data. This project builds a pipeline that:

- Automates ingestion and transformation of raw job data
- Data load from the API by using dlt(data load tool)
- Stores it in an AWS-based lakehouse architecture (S3 + Redshift)
- Transforms the data using dbt
- Visualizes insights on job types, e-filing, equipment usage, and building types

The goal: enable stakeholders to explore trends in construction filings via an easy-to-use dashboard.

---

## ☁️ Cloud Setup

- All services are deployed using **AWS**:
  - Redshift Serverless (data warehouse)
  - S3 (data lake)
  - AWS Glue (catalog)
  - IAM Roles for permissioning
- Infrastructure provisioned using **Terraform** as IaC(Infrastructure as code)

---

## 📦 Pipeline Overview (Batch)

This is a **batch pipeline**, scheduled to run daily via Airflow.

### Pipeline Steps:

1. **DLT Ingestion**: Calls NYC DOB Job API and stores data as Parquet in local FS
2. **S3 Upload**: Moves data to S3
3. **Glue Crawler**: Catalogs data into AWS Glue Data Catalog
4. **Redshift Spectrum**: Creates external table from Glue catalog
5. **Internal Copy**: Copies raw data from Spectrum into Redshift internal table
6. **dbt Transform**: Cleans, models, and tests data
7. **Metabase Dashboard**: Loads data for business visualization

Orchestrated via **Airflow DAG** with all tasks automated.

---

## 🧰 Tools & Tech

| Layer                | Tool                        |
|---------------------|-----------------------------|
| Ingestion           | DLT                         |
| Data Lake           | AWS S3                      |
| Catalog             | AWS Glue                    |
| DWH                 | Redshift + Spectrum         |
| Transformations     | dbt                         |
| Orchestration       | Apache Airflow              |
| Visualization       | Metabase                    |
| IaC                 | Terraform                   |
| Language            | Python                      |
| Containerization    | Docker + docker-compose     |

---

## 🧪 dbt Transformations

- `stg_dob_jobs.sql`: staging model from raw data
- `cleaned_jobs.sql`: final analytics model
- Uses `dbt test` to validate schema and nulls
- Materialized as tables in `analytics` schema

---

## 📊 Dashboard (Metabase)

Dashboard accessible via Metabase with:


![Dashboard](./Data-Dashbord/dash-board.mov)

---

## 🛠️ Infrastructure with Terraform

Provisioned using `terraform/`:

- Redshift Serverless Workgroup
- IAM Role for Redshift Spectrum
- Glue Database + Crawler
- S3 Path & Permissions

State files are excluded via `.gitignore`.

## 📁 Project Structure

DOB-JOB-DE-PROJECT/
├── dags/                         # Airflow DAGs and dbt project
│   ├── dob_dbt_project/          # dbt transformations
│   │   ├── analyses/
│   │   ├── macros/
│   │   ├── models/
│   │   ├── seeds/
│   │   ├── snapshots/
│   │   ├── tests/
│   │   ├── dbt_project.yml
│   │   ├── profiles.yml
│   │   └── .gitignore
│   └── full_pipeline_dag.py      # Airflow DAG to run the pipeline
│
├── job-dlt-pipeline/             # DLT ingestion pipeline
│   ├── .dlt/
│   │   ├── config.toml    # (Should be gitignored)
│   │   └── secrets.toml   # (Should be gitignored)
│   ├── rest_api_pipeline.py
│   └── .gitignore
│
├── scripts/                      # Custom scripts for AWS, Redshift, etc.
│   ├── copy_to_redshift.py
│   ├── create_external_schema.py
│   ├── metabase_automation.py
│   └── run_glue_crawler.py
│
├── terraform/                    # Infrastructure as Code (Terraform)
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── terraform.tfvars          # (Should be gitignored)
│   ├── terraform.tfstate         
│   ├── .terraform/               # (Should be gitignored)
│   ├── .terraform.lock.hcl
│   └── .gitignore
│
├── Dockerfile                    # Custom Airflow image
├── docker-compose.yaml           # Run Airflow + Metabase
├── requirements.txt              # Python dependencies
├── data_column_read.ipynb        # EDA notebook
├── .env                          # Actual secrets (excluded from Git)
├── .env.example                  # Example env file
├── .gitignore
├── README.md                     # Project documentation
└── Data-Dashboard/
    └── nyc_dob_dashboard.png     # Image for README preview



---

## 💻 Reproducibility

### 1. Clone this repo & setup env

```bash
git clone https://github.com/YOUR_USERNAME/nyc-dob-job-pipeline.git
cd nyc-dob-job-pipeline



Fill in:

- AWS keys
- Redshift credentials
- IAM role
- Metabase user
- dlt secret.toml

Run containers

- docker-compose up --build

✅ Airflow: http://localhost:8080
✅ Metabase: http://localhost:3000

Trigger DAG in Airflow to run full pipeline.

Bonus Improvements
✅ Airflow DAG with clear dependencies
✅ Automated Metabase dashboard creation
✅ Modular repo with separate folders per tool
✅ .gitignore for security


