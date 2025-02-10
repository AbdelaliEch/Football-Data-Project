# Data Engineering Zoomcamp 2025 - Final Project

Quick Links: [Looker Studio Data Visualization](https://lookerstudio.google.com/reporting/70c08dd6-9771-41d6-a549-ab60b1409b00)

![Players Dashboard](https://github.com/AbdelaliEch/final_project/blob/main/images/Players%20Dashboard.jpg)

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
This project is part of the **Data Engineering Zoomcamp 2025** and serves as the capstone project required to complete the course. The project aims to build an end-to-end data pipeline using cloud infrastructure, orchestration tools, and distributed computing technologies.

## Project Overview
The objective of this project is to extract a dataset from Kaggle, process it using Apache Spark, store the processed data in Google Cloud Storage (GCS) and BigQuery, transform it with dbt, and visualize insights using Looker Studio.

## Data Pipeline
The data pipeline follows a structured process:
1. **Extract**: Download the dataset from Kaggle and store it in Google Cloud Storage (GCS).
2. **Load**: Provision GCS bucket and BigQuery dataset using Terraform.
3. **Transform**: Process data using Apache Spark and load the results into BigQuery.
4. **Model**: Utilize dbt to create staging, intermediate, and final models.
5. **Visualize**: Create dashboards and insights in Looker Studio.

## Tools and Technologies Used
- **Google Cloud Platform (GCP)**: Includes Compute Engine, Cloud Storage, BigQuery, Dataproc
- **Terraform**: Infrastructure as code for provisioning GCP resources
- **Kestra**: Workflow orchestration tool for managing the ETL pipeline
- **Docker & Docker Compose**: Containerization for environment setup
- **Apache Spark**: Distributed computing for data processing
- **dbt Cloud**: Data modeling and transformation
- **Looker Studio**: Data visualization for interactive dashboards
- **Kaggle API**: Data extraction from Kaggle

## Step-by-Step Implementation
### 1. Setting up GCP
- Created a **Google Cloud Platform (GCP)** account and project.
- Followed [this video](https://youtu.be/ae-CV2KfoN0?si=jq2KO6LgsO2F_D_v) for setting up a **Virtual Machine (VM)**.

### 2. Infrastructure Setup with Terraform
- Provisioned **Google Cloud Storage (GCS) bucket** and **BigQuery dataset** using Terraform.
  - Terraform scripts are available in the repository under the `/terraform` directory.

### 3. Kestra Workflow Setup
- Installed **Kestra** using Docker Compose.
- Configured **GCP credentials** in `kestra_flows/gcp_kv.yaml`.
- Implemented a **Kaggle data extraction and upload flow** (`kestra_flows/kaggle_download_gcs_upload.yaml`).

### 4. Apache Spark Setup
- Installed **Apache Spark (version 3.4.4)** locally on the VM.
  - Refer to the [installation guide](https://youtu.be/hqUbB9c8sKg?si=coujzlSGM3fRzqKz).
- Linked **Spark** with **Google Cloud Storage** for data processing.
  - [Tutorial on connecting Spark with GCS](https://youtu.be/Yyz293hBVcQ?si=ei5qu9n9NXTVTf2n).
- Created a **Jupyter notebook** for testing Spark with GCS (`notebooks/spark_gcs.ipynb`).

### 5. Processing Data with Dataproc
- Converted the Jupyter notebook to a Python script (`notebooks/spark_gcs_bigquery.py`).
- Uploaded the script to GCS and ran the **Dataproc job** on the Google Cloud Platform:
  ```bash
  gcloud dataproc jobs submit pyspark \
      --cluster=project-cluster-2c88 \
      --region=europe-west2 \
      --jars=gs://spark-lib/bigquery/spark-3.4-bigquery-0.37.0.jar \
      gs://de-zoomcamp-project-449906_bucket/code/spark_gcs_bigquery.py

### 6. Data Modeling with dbt Cloud
- Set up **dbt Cloud** for data modeling.
  - Followed the [Setup Guide](https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/tree/main/4_Analytics-Engineering) and the [DataTalksClub Guide](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/dbt_cloud_setup.md).
- Configured **BigQuery connection** in dbt Cloud.
- Built **staging, intermediate, and mart models** in dbt to prepare the data for analysis and visualization.
- Added **tests** and **documentation** for each model to ensure data quality and pipeline reliability.

### 7. Visualization with Looker Studio
- Created an interactive **Looker Studio dashboard** to display insights from the processed data.
  - The dashboard visualizes key metrics and aggregated trends from the transformed data.
  - You can access the dashboard [here](https://lookerstudio.google.com/reporting/70c08dd6-9771-41d6-a549-ab60b1409b00).

### Reproducibility
To reproduce the project, follow these steps:
1. **Setup GCP & Terraform**: Run the Terraform scripts located in the `/terraform` directory to provision GCP infrastructure (such as GCS buckets and BigQuery datasets).
2. **Deploy Kestra**: Use Docker Compose to deploy the Kestra orchestrator on your local machine.
3. **Run the ETL pipeline**: Execute the Kestra flows to handle data extraction, processing, and uploading.
4. **Process Data with Apache Spark**: Submit the Spark job to Dataproc to process and transform the data.
5. **Model Data with dbt**: Use dbt Cloud to build and deploy staging, intermediate, and mart models.
6. **Visualize Data in Looker Studio**: Connect your BigQuery dataset to Looker Studio and create dashboards for analysis.

### Dashboard and Visualization
The final dataset is visualized in an interactive **Looker Studio dashboard**, which includes:
- **Summary statistics**: Overview of key metrics from the processed data.
- **Aggregated trends**: Visualizations of long-term trends and correlations.
- **Key performance indicators (KPIs)**: Insights derived from the dbt models, showing the most relevant data points for analysis.

### Future Enhancements
- Implement **CI/CD pipelines** to automate deployments for Spark jobs and dbt models.
- Add **Airflow/Kestra scheduling** to automate data pipeline execution and updates.
- Integrate **Great Expectations** to improve **data quality testing** and ensure pipeline reliability.

