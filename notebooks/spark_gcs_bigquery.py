#!/usr/bin/env python
# coding: utf-8

import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext


spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

spark.conf.set('temporaryGcsBucket', 'dataproc-temp-europe-west2-621212701441-3vr0wlvx')


files = ["appearances", "club_games", "clubs", "competitions", "game_events", 
         "game_lineups", "games", "player_valuations", "players", "transfers"]

dfs = {
    file: spark.read \
           .option('header', 'true') \
           .option("inferSchema", True) \
           .csv(f'gs://de-zoomcamp-project-449906_bucket/raw/{file}.csv') 
    for file in files
}


for file in dfs.keys():
    output_path = f'gs://de-zoomcamp-project-449906_bucket/pq/{file}/'
    # we'll use coalesce on small files that spark don't handle properly
    if file in ['club_games', 'players', 'games', 'player_valuations', 'transfers']:
        dfs[file].coalesce(1).write.parquet(output_path, mode='overwrite')
    else:
        dfs[file].write.parquet(output_path, mode='overwrite')


pq_dfs = {
    file: spark.read \
           .parquet(f'gs://de-zoomcamp-project-449906_bucket/pq/{file}/') 
    for file in files
}

for file in pq_dfs.keys():
    output_table_path = f'de-zoomcamp-project-449906.de_zoomcamp_project_dataset.{file}'
    pq_dfs[file].write.format('bigquery') \
        .option('table', output_table_path) \
        .save()