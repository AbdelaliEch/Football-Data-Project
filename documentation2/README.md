# Data Engineering Zoomcamp 2025 - Final Project

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Data Pipeline](#data-pipeline)
- [Tools and Technologies Used](#tools-and-technologies-used)
- [Step-by-Step Implementation](#step-by-step-implementation)
- [Reproducibility](#reproducibility)
- [Dashboard and Visualization](#dashboard-and-visualization)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Introduction
This project is part of the **Data Engineering Zoomcamp 2025** and serves as the capstone project required to complete the course. It involves building an end-to-end data pipeline using cloud infrastructure, orchestration tools, and distributed computing.

## Project Overview
The goal of this project is to extract a dataset from Kaggle, process it using Apache Spark, store it in Google Cloud Storage (GCS) and BigQuery, transform it using dbt, and visualize insights with Looker Studio.

## Data Pipeline
The project follows a structured data pipeline:
1. **Extract**: Download dataset from Kaggle and store it in GCS.
2. **Load**: Use Terraform to create a GCS bucket and BigQuery dataset.
3. **Transform**: Process data using Apache Spark and load results into BigQuery.
4. **Model**: Use dbt to create staging, intermediate, and final models.
5. **Visualize**: Build dashboards in Looker Studio.

## Tools and Technologies Used
- **Google Cloud Platform (GCP)**: Compute Engine, Cloud Storage, BigQuery, Dataproc
- **Terraform**: Infrastructure as code for provisioning GCP resources
- **Kestra**: Workflow orchestration
- **Docker & Docker Compose**: Containerization
- **Apache Spark**: Distributed computing for data processing
- **dbt Cloud**: Data modeling and transformation
- **Looker Studio**: Dashboard visualization
- **Kaggle API**: Data extraction

## Step-by-Step Implementation
### 1. Setting up GCP
- Created a new **GCP account** and started a project.
- Followed [this video](https://youtu.be/ae-CV2KfoN0?si=jq2KO6LgsO2F_D_v) to create and set up a Virtual Machine (VM).

### 2. Infrastructure Setup with Terraform
- Created **GCS bucket** and **BigQuery dataset** using Terraform.

### 3. Kestra Workflow Setup
- Installed **Kestra** using Docker Compose.
- Configured **GCP credentials** using `kestra_flows/gcp_kv.yaml`.
- Implemented a **Kaggle data extraction and upload flow** (`kestra_flows/kaggle_download_gcs_upload.yaml`).

### 4. Apache Spark Setup
- Installed Spark **(version 3.4.4)** locally on the VM ([installation guide](https://youtu.be/hqUbB9c8sKg?si=coujzlSGM3fRzqKz)).
- Linked **Spark with GCS** ([tutorial](https://youtu.be/Yyz293hBVcQ?si=ei5qu9n9NXTVTf2n)).
- Created a Jupyter notebook (`notebooks/spark_gcs.ipynb`) for testing.

### 5. Processing Data with Dataproc
- Converted the test notebook to a Python script: `notebooks/spark_gcs_bigquery.py`.
- Uploaded script manually to GCS (due to `gsutil cp` permission issues).
- Ran the Dataproc job:
  ```bash
  gcloud dataproc jobs submit pyspark \
      --cluster=project-cluster-2c88 \
      --region=europe-west2 \
      --jars=gs://spark-lib/bigquery/spark-3.4-bigquery-0.37.0.jar \
      gs://de-zoomcamp-project-449906_bucket/code/spark_gcs_bigquery.py
  ```

### 6. Data Modeling with dbt Cloud
- Set up **dbt Cloud** by following:
  - [Setup Guide](https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/tree/main/4_Analytics-Engineering)
  - [DataTalksClub Guide](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/dbt_cloud_setup.md)
- Configured **BigQuery connection** in dbt.
- Built **staging, intermediate, and mart models**.
- Added **tests and documentation**.

### 7. Visualization with Looker Studio
- Created a **Looker Studio dashboard** to display key insights.

## Reproducibility
To reproduce this project:
1. **Setup GCP & Terraform**: Provision infrastructure using Terraform scripts.
2. **Deploy Kestra**: Run Docker Compose to start the orchestrator.
3. **Run the ETL pipeline**: Execute Kestra flows to extract and upload data.
4. **Process with Spark**: Run Spark job on Dataproc.
5. **Transform data with dbt**: Build and deploy dbt models.
6. **Visualize in Looker Studio**: Connect BigQuery and create dashboards.

## Dashboard and Visualization
The final dataset is visualized in a **Looker Studio dashboard**, which includes:
- **Summary statistics** of the dataset
- **Aggregated trends** based on transformations
- **Key performance indicators** derived from dbt models

## Future Enhancements
- Implement **automated CI/CD pipelines** for dbt and Spark scripts.
- Add **Airflow/Kestra scheduling** for real-time updates.
- Improve **data quality tests** using Great Expectations.

## Contributors
- **[Your Name]** (your.email@example.com)

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to **DataTalks.Club** and the creators of the **Data Engineering Zoomcamp** for the valuable learning experience.

