# Football Data Engineering Project

Quick Links: [Looker Studio Data Visualization](https://lookerstudio.google.com/reporting/70c08dd6-9771-41d6-a549-ab60b1409b00) | [Grading guide](https://github.com/AbdelaliEch/final_project/blob/main/grading_guide.md)

![Players Dashboard](https://github.com/AbdelaliEch/final_project/blob/main/images/Players%20Dashboard.jpg)

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Data Pipeline](#data-pipeline)
- [Tools and Technologies Used](#tools-and-technologies-used)
- [Step-by-Step Implementation](#step-by-step-implementation)
- [Reproducibility](#reproducibility)
- [Acknowledgments](#acknowledgments)

---

## Introduction
This project is part of the **Data Engineering Zoomcamp 2025** and serves as the capstone project required to complete the course. The project aims to build an end-to-end data pipeline using cloud infrastructure, orchestration tools, and distributed computing technologies.

## Problem Description and Project Objective
Football is one of the most popular sports worldwide, generating vast amounts of data related to players, clubs, competitions, and transfers. However, accessing and analyzing this data efficiently can be challenging due to its size, complexity, and inconsistency.  

This project aims to solve the following problems:  
- **Data Accessibility**: Raw football data is often scattered across different sources, making it difficult to consolidate and analyze.  
- **Data Cleaning & Processing**: The dataset contains inconsistencies and missing values that need to be handled before analysis.  
- **Scalability**: Processing large datasets manually or on local machines can be inefficient and time-consuming.  
- **Visualization & Insights**: Even when the data is cleaned, drawing meaningful insights from it requires intuitive and interactive visualizations.  

By building a structured ELT pipeline using cloud technologies, distributed computing, and automated workflows, this project enables efficient data processing, storage, and visualization, providing users with valuable insights into football statistics.  

## Dataset
The raw dataset we used consists of the following files:
- `appearances.csv`
- `players.csv`
- `games.csv`
- `clubs.csv`
- `club_games.csv`
- `game_lineups.csv`
- `player_valuations.csv`
- `transfers.csv`
- `competitions.csv`  

You can access the dataset on Kaggle [here](https://www.kaggle.com/datasets/davidcariboo/player-scores).  
> **Note**: Please be aware that some of the data may not be 100% accurate or clean. During the data processing and transforming phases, some inconsistencies were addressed and certain records were cleaned to ensure the pipeline functions smoothly. As a result, some statistics may not be entirely precise due to the original dataset's nature.

## Data Pipeline
The data pipeline follows a structured ELT (Extract, Load, Transform) process:
1. **Extract**: Download raw csv football data from Kaggle and store it in Google Cloud Storage (GCS).
2. **Load and Process**: Use Apache Spark to process the csv data directly from GCS, convert it to Parquets and then reload the processed data back to both GCS and BigQuery.
3. **Transform**: Utilize dbt to transform the data in BigQuery, creating staging, intermediate, and mart models.
5. **Visualize**: Build dashboards and insights in Looker Studio to visualize the results.

## Tools and Technologies Used
- **Google Cloud Platform (GCP)**: Includes Compute Engine, Cloud Storage, BigQuery, Dataproc
- **Terraform**: Infrastructure as code for provisioning GCP resources
- **Kestra**: Workflow orchestration tool for managing the ELT pipeline
- **Docker & Docker Compose**: Containerization for environment setup
- **Apache Spark**: Distributed computing for data processing
- **dbt Cloud**: Data modeling and transformation
- **Looker Studio**: Data visualization for interactive dashboards

## Step-by-Step Implementation
### 1. Setting up GCP
- Created a **Google Cloud Platform (GCP)** new project.
- Followed [this video](https://youtu.be/ae-CV2KfoN0?si=jq2KO6LgsO2F_D_v) for setting up a **Virtual Machine (VM)**.

### 2. Infrastructure Setup with Terraform
- Provisioned **Google Cloud Storage (GCS) bucket** and **BigQuery dataset** using Terraform.
  - Terraform script is available in the repository under the `/terraform` directory.

### 3. Kestra Setup: Data Extraction and Loading Workflow
- Installed **Kestra** using Docker Compose.
  - The docker-compose file used is in `docker-compose.yaml` file located in the root directory.
- Configured **GCP credentials** using Kestra to store the necessary GCP credentials to enable Kestra to interact with Google Cloud services
  - The flow used is in `kestra_flows/gcp_kv.yaml` file.
- Implemented a **Kaggle data extraction and upload to GCS flow**
  - The flow used is in `kestra_flows/kaggle_download_gcs_upload.yaml` file.

### 4. Apache Spark Setup
- Installed **Apache Spark (version 3.4.4)** locally (for testing the data) on the VM.
  - Refer to the [installation guide](https://youtu.be/hqUbB9c8sKg?si=coujzlSGM3fRzqKz).
- Created a **Jupyter notebook** and linked **Spark** with **Google Cloud Storage** to analyze the files columns and schema using Spark Dataframes.
  - [Tutorial on connecting Spark with GCS](https://youtu.be/Yyz293hBVcQ?si=ei5qu9n9NXTVTf2n).
  - The jupyter notebook file is in `notebooks/spark_gcs.ipynb`.

### 5. Processing Data with Dataproc
- **Set up Dataproc cluster**: Followed this [video](https://youtu.be/osAiAYahvh8?si=QDfmIj-xN3DZD7Yd) to set up the Dataproc cluster on Google Cloud Platform.
- Converted the previous Jupyter notebook to a Python script and modified it to make it convert the CSV data to Parquets and then reload the processed parquets data back to both GCS and BigQuery.
  - The python script is in `notebooks/spark_gcs_bigquery.py`.
- Uploaded the script to GCS and ran the **Dataproc job** using the command:
  ```bash
  gcloud dataproc jobs submit pyspark \
      --cluster=project-cluster-2c88 \
      --region=europe-west2 \
      --jars=gs://spark-lib/bigquery/spark-3.4-bigquery-0.37.0.jar \
      gs://de-zoomcamp-project-449906_bucket/code/spark_gcs_bigquery.py
  ```

### 6. Data Transformation with dbt Cloud
- Set up **dbt Cloud** for data transformation.
  - Followed the [Setup Guide](https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/tree/main/4_Analytics-Engineering) and the [DataTalksClub Guide](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/dbt_cloud_setup.md).
- Configured **BigQuery connection** in dbt Cloud.
- Built **staging, intermediate, and mart models** in dbt to prepare the data for analysis and visualization along with tests and documentation to ensure data quality and pipeline reliability.
  - The full dbt project is available in the repository under the `/dbt-project` directory

 
### 7. Visualization with Looker Studio
- Created an interactive **Looker Studio dashboard** to display key insights from the data processed and transformed.
- The dashboard is divided into **5 pages**, each providing specific insights and enabling data exploration:
  1. **Players Dashboard**:
     - Users can filter by **Player** and **Season** to view detailed statistics for a specific player during a given season or across multiple seasons.
  2. **Clubs Dashboard**:
     - Users can filter by **Club** and **Season** to explore statistics for a specific club during a given season or across multiple seasons.
  4. **Competitions Dashboard**:
     - Allows filtering by **Competition** and **Season** to view competition-specific statistics, including performance data for each season.
  6. **Transfers Dashboard**:
     - Displays transfer-related data, allowing users to filter by **Season** to see transfers trends.
  7. **Additional Statistics**:
     - Provides aggregated statistics such as **Total Goals** and **Total Assists** by **Country**. 
- You can access the dashboard [here](https://lookerstudio.google.com/reporting/70c08dd6-9771-41d6-a549-ab60b1409b00).

## Reproducibility
To reproduce this project, follow the exact same steps outlined in the **Step-by-Step Implementation** section above.

## Acknowledgments
Special thanks to **DataTalks.Club** and all the instructors of the **Data Engineering Zoomcamp** for the valuable learning experience.
