# Final-Project

1) Created a GCP account and started a new project: "de-zoomcamp-project" 
2) I followed the instructions in this video: https://youtu.be/ae-CV2KfoN0?si=jq2KO6LgsO2F_D_v to create a VM "project-vm" and set it up. 
3) Created a gcs bucket "de-zoomcamp-project-449906_bucket" and bigquery dataset "de_zoomcamp_project_dataset" using Terraform 
4) Kestra setup with docker using Docker-compose
5) Setup GCP credentials in Kestra using "gcp_kv" flow
6) Extract dataset from Kaggle and upload it to GCS bucket using "kaggle_download_gcs_upload" flow


Now let's start the pipeline
First we need to use a kestra workflow that will extract the data from Kaggle and upload it GCS bucket
I already have the download task done, we still need the upload task

