# Football Data Engineering Project

Quick Links: [Looker Studio Data Visualization](https://lookerstudio.google.com/reporting/70c08dd6-9771-41d6-a549-ab60b1409b00) | Reproduction Guide
![Players Dashboard](https://github.com/AbdelaliEch/final_project/blob/main/images/Players%20Dashboard.jpg)

## Overview
This project focuses on building a **dashboard** using football data sourced from **Transfermarkt**. The dataset contains multiple CSV files, including details on players, clubs, games, appearances, valuations, and transfers. The project follows a structured data engineering workflow using **Google Cloud Platform (GCP)**, **Kestra**, **Spark**, **BigQuery**, **dbt**, and **Looker Studio**.

## Dataset
The dataset consists of the following files:
- `appearances.csv`
- `players.csv`
- `games.csv`
- `clubs.csv`
- `club_games.csv`
- `game_lineups.csv`
- `player_valuations.csv`
- `transfers.csv`
- `competitions.csv`

## Project Architecture & Steps

### 1. **GCP Setup**
- Created a **GCP account** and started a new project.
- Set up a **VM instance** following [this guide](https://youtu.be/ae-CV2KfoN0?si=jq2KO6LgsO2F_D_v).

### 2. **Storage & Infrastructure**
- Used **Terraform** to create a **GCS bucket** and a **BigQuery dataset**.
- Installed **Kestra** using Docker (`docker-compose`).
- Configured **GCP credentials** in Kestra using `kestra_flows/gcp_kv.yaml`.

### 3. **Data Extraction & Storage**
- Extracted the dataset from **Kaggle** and uploaded it to **GCS** using `kestra_flows/kaggle_download_gcs_upload.yaml`.
- Installed **Spark 3.4.4** locally on the VM following [this guide](https://youtu.be/hqUbB9c8sKg?si=coujzlSGM3fRzqKz).
- Linked **Spark with GCS** using [this tutorial](https://youtu.be/Yyz293hBVcQ?si=ei5qu9n9NXTVTf2n) and performed exploratory testing.

### 4. **Data Processing with Spark & Dataproc**
- Converted the testing Jupyter notebook (`notebooks/spark_gcs.ipynb`) into a Python script (`notebooks/spark_gcs_bigquery.py`).
- Manually uploaded the script to the **GCS bucket** (due to `gsutil cp` permission issues).
- Submitted a **Dataproc job** using the following command:

```bash
gcloud dataproc jobs submit pyspark \
    --cluster=project-cluster-2c88 \
    --region=europe-west2 \
    --jars=gs://spark-lib/bigquery/spark-3.4-bigquery-0.37.0.jar \
    gs://de-zoomcamp-project-449906_bucket/code/spark_gcs_bigquery.py
```

### 5. **Analytics & Transformation with dbt**
- Set up a **dbt cloud project** following these guides:
  - [Manuel Guerra's Notes](https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/tree/main/4_Analytics-Engineering)
  - [DataTalksClub's dbt setup](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/dbt_cloud_setup.md)
- Configured **BigQuery connection** in dbt cloud (ensuring region consistency).
- Created **staging, intermediate, and mart models**.
- Added **tests and documentation**.

### 6. **Visualization with Looker Studio**
- Built an **interactive dashboard** using **Looker Studio** to visualize key insights.

## Results & Future Improvements
### Key Deliverables:
✅ **Data Pipeline**: Automated extraction, transformation, and loading (ETL) from Kaggle to BigQuery.  
✅ **dbt Models**: Well-structured staging, intermediate, and mart layers.  
✅ **Looker Studio Dashboard**: Visualization of key football insights.  

### Potential Improvements:
- Automate the `spark_gcs_bigquery.py` upload process.
- Implement better monitoring/logging in Kestra.
- Extend analysis with **Machine Learning models**.

## How to Reproduce
1. Set up a **GCP project**.
2. Use **Terraform** to create GCS and BigQuery.
3. Deploy **Kestra** and configure credentials.
4. Run the **data ingestion flow** (`kestra_flows/kaggle_download_gcs_upload.yaml`).
5. Process data using **Spark & Dataproc** (`notebooks/spark_gcs_bigquery.py`).
6. Set up **dbt models** and run transformations.
7. Build a **Looker Studio dashboard** for visualization.

## Conclusion
This project showcases an end-to-end **data engineering pipeline** for football analytics, integrating GCP, Spark, BigQuery, dbt, and Looker Studio. 🚀

