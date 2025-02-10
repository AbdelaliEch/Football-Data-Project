# Final-Project

1) Created a GCP account and started a new project  
2) I followed the instructions in this video: https://youtu.be/ae-CV2KfoN0?si=jq2KO6LgsO2F_D_v to create a VM and set it up.   
3) Created a gcs bucket and bigquery dataset using Terraform   
4) Kestra setup with docker using Docker-compose  
5) Setup GCP credentials in Kestra using "kestra_flows/gcp_kv.yaml" flow  
6) Extract dataset from Kaggle and upload it to GCS bucket using "kestra_flows/kaggle_download_gcs_upload.yaml" flow  
7) Installed Spark locally (for testing) on the VM using this video: https://youtu.be/hqUbB9c8sKg?si=coujzlSGM3fRzqKz  
But I didn't use the same version in the video, I installed spark 3.4.4  
Then I linked spark with GCS in the "notebooks/spark_gcs.ipynb" notebook using this video: https://youtu.be/Yyz293hBVcQ?si=ei5qu9n9NXTVTf2n   
And did some testing on the files to know the fields, sizes, schema...  
8) Converted the testing "notebooks/spark_gcs.ipynb" notebook into python file "notebooks/spark_gcs_bigquery.py" and modified it, 
so that we can use it with dataproc  
Remark: I needed the file "notebooks/spark_gcs_bigquery.py" in my bucket, gsutil cp command didn't work for me even tough my VM service account
had all the necessary permissions.
So I uploaded the file manually by downloading it from vscode to my local computer then using GCP GUI to upload it  
Then I ran this command:
```bash
gcloud dataproc jobs submit pyspark \
    --cluster=project-cluster-2c88 \
    --region=europe-west2 \
    --jars=gs://spark-lib/bigquery/spark-3.4-bigquery-0.37.0.jar \
    gs://de-zoomcamp-project-449906_bucket/code/spark_gcs_bigquery.py
```
9) Setup dbt project on dbt cloud by following these instructions:        
https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/tree/main/4_Analytics-Engineering   
https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/dbt_cloud_setup.md  
when setuping the bigquery connection, after uploading key json file, click ctrl+f > type 'location' > location >
type the same location you have in your bigquery dataset (for example europe-west2, ....)
10) Create dbt staging, intermediate and mart models
11) Added tests and documentation
12) Made a Looker studio dashboard


Next step: 
    - Documenting the whole project in this README file
