# Football Data Engineering Project

Quick Links: [Looker Studio Data Visualization](https://lookerstudio.google.com/reporting/467df289-21d8-4cfd-8f27-a890f698a903) | [Grading guide](https://github.com/AbdelaliEch/Football-Data-Project/blob/main/grading_guide.md)

![Players Dashboard](https://github.com/AbdelaliEch/Football-Data-Project/blob/main/images/Players%20Dashboard.jpg)

## Table of Contents
- [Introduction](#introduction)
- [Problem description and Project objective](#problem-description-and-project-objective)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Data Pipeline](#data-pipeline)
- [Step-by-Step Implementation](#step-by-step-implementation)
- [Reproducibility](#reproducibility)
- [Acknowledgments](#acknowledgments)

---

## Introduction
This project is part of the **Data Engineering Zoomcamp 2025** and serves as the capstone project required to complete the course. This project aims to build an end-to-end data pipeline leveraging cloud infrastructure, orchestration tools, and distributed computing technologies.

## Problem Description and Project Objective
Football is one of the most popular sports worldwide, generating vast amounts of data related to players, clubs, competitions, and transfers. However, accessing and analyzing this data efficiently can be challenging due to its size, complexity, and inconsistency.  

This project aims to solve the following problems:  
- **Data Accessibility**: Raw football data is often scattered across different sources, making it difficult to consolidate and analyze.  
- **Data Cleaning & Processing**: The dataset contains inconsistencies and missing values that need to be handled before analysis.  
- **Scalability**: Processing large datasets manually or on local machines can be inefficient and time-consuming.  
- **Visualization & Insights**: Even when the data is cleaned, drawing meaningful insights from it requires intuitive and interactive visualizations.  

By implementing a structured ELT pipeline with cloud technologies, distributed computing, and automated workflows, this project facilitates efficient data processing, storage, and visualization, delivering valuable insights into football statistics.  

## Dataset
The raw dataset used consists of the following files:
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
> **Note**: Please be aware that some of the data may not be 100% accurate and clean. During the data processing and transforming phases, some inconsistencies were addressed and certain records were cleaned to ensure the pipeline functions smoothly. As a result, some statistics may not be entirely precise due to the original dataset's nature.

## Tech Stack  
- **Cloud Platform:** Google Cloud Platform (GCP)  
- **Infrastructure as Code:** Terraform  
- **Orchestration:** Apache Airflow  
- **Data Processing:** PySpark (Dataproc)  
- **Data Transformation:** dbt Cloud  
- **Storage & Warehousing:** Google Cloud Storage (GCS), BigQuery  
- **Visualization:** Looker Studio 

## Data Pipeline
![Pipeline Diagram](https://github.com/AbdelaliEch/Football-Data-Project/blob/main/images/Pipeline%20diagram.png)
The data pipeline follows a structured ELT (Extract, Load, Transform) process:
1. **Extract**: Download raw csv football data from Kaggle and store it in Google Cloud Storage (GCS).
2. **Process and Load**:  
   - A **Dataproc PySpark job** is submitted to process and clean the data.  
   - It reads the raw CSV files from GCS.  
   - Performs necessary processing, cleaning, and filtering on the raw data.  
   - The cleaned data is then loaded into **BigQuery** as tables.
3. **Transform**: Utilize dbt to transform the data in BigQuery, creating staging, intermediate, and mart models.
4. **Visualize**: Build dashboards and insights in Looker Studio to visualize the results.

## Step-by-Step Implementation
### 1. Setting up GCP and VM
- Created a **Google Cloud Platform (GCP)** new project.
- Deployed a **Virtual Machine (VM)** following [this setup guide](https://youtu.be/ae-CV2KfoN0?si=jq2KO6LgsO2F_D_v).  

### 2. Infrastructure Setup with Terraform
- Provisioned **Google Cloud Storage (GCS) bucket** and **BigQuery datasets** using [Terraform script](https://github.com/AbdelaliEch/Football-Data-Project/blob/main/terraform/main.tf).

### 3. Developing Data Processing & Transformation Scripts  
- Developed a **PySpark script** to process raw data from gcs and upload it to Bigquery in tables format.  
  - 📜 [PySpark script](https://github.com/AbdelaliEch/Football-Data-Project/blob/main/dataproc_script.py)  
- Created a **dbt Cloud project** and built staging, intermediate, and mart models to prepare data for analysis.  
  - 📂 [dbt models](https://github.com/AbdelaliEch/Football-Data-Project/tree/main/dbt_project/models) 
  - 📂 [dbt full project](https://github.com/AbdelaliEch/Football-Data-Project/tree/main/dbt_project) 
  - Included **tests and documentation** to ensure data quality and pipeline reliability.

### 4. Automating the Data Pipeline with Airflow  
Once the data processing and transformation scripts were developed, **Apache Airflow** was used to automate the end-to-end pipeline
- Set up **Astronomer Airflow Docker** by following [this tutorial](https://academy.astronomer.io/path/airflow-101/local-development-environment).  
- Configured necessary connections in Airflow UI (**Kaggle, GCP, and dbt Cloud**).   
#### 🔹 DAG Workflow  
1. **Download Dataset from Kaggle** → Fetches football player statistics via the Kaggle API.  
2. **Upload Dataset to GCS** → Stores raw data in a **Google Cloud Storage (GCS) bucket**.  
3. **Process Data with PySpark on Dataproc** → Runs a PySpark job on **Google Dataproc** to clean and preprocess data before loading it into **BigQuery**.  
4. **Transform Data using dbt** → Runs dbt models to structure and optimize data in **BigQuery**.  

🔗 **[View the full Airflow DAG](https://github.com/AbdelaliEch/Football-Data-Project/blob/main/airflow/dags/project_dag.py)**  

### 5. Visualization with Looker Studio
- Created an interactive **Looker Studio dashboard** to display key insights from the data processed and transformed.
- The dashboard is divided into **5 pages**, each providing specific insights and enabling data exploration:
  1. **Players Dashboard**:
     - Users can filter by **Player** and **Season** to view detailed statistics for a specific player during a given season or across multiple seasons.
  2. **Clubs Dashboard**:
     - Users can filter by **Club** and **Season** to explore statistics for a specific club during a given season or across multiple seasons.
  3. **Competitions Dashboard**:
     - Allows filtering by **Competition** and **Season** to view competition-specific statistics, including performance data for each season.
  4. **Transfers Dashboard**:
     - Displays transfer-related data, allowing users to filter by **Season** to see transfers trends.
  5. **Additional Statistics**:
     - Provides aggregated statistics such as **Total Goals** and **Total Assists** by **Country**. 
- You can access the full Looker studio report [here](https://lookerstudio.google.com/reporting/467df289-21d8-4cfd-8f27-a890f698a903).

## Reproducibility
To reproduce this project, follow the Step-by-Step Implementation section above, which provides clear and detailed instructions for easy replication.

## Acknowledgments
Special thanks to **DataTalks.Club**, the instructors of the **Data Engineering Zoomcamp** and all the **Slack community** for the valuable learning experience.
