# Football Data Engineering Project

Quick Links: [Looker Studio Data Visualization](https://lookerstudio.google.com/reporting/70c08dd6-9771-41d6-a549-ab60b1409b00) 

![Players Dashboard](https://github.com/AbdelaliEch/final_project/blob/main/images/Players%20Dashboard.jpg)

## Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Dataset](#dataset)
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
- **Kestra**: Workflow orchestration tool for managing the ELT pipeline
- **Docker & Docker Compose**: Containerization for environment setup
- **Apache Spark**: Distributed computing for data processing
- **dbt Cloud**: Data modeling and transformation
- **Looker Studio**: Data visualization for interactive dashboards
- **Kaggle API**: Data extraction from Kaggle
