#!/usr/bin/env python
# coding: utf-8

import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import functions as F



spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

spark.conf.set('temporaryGcsBucket', '<dataproc temp bucket>')


df_appearances = spark.read.csv('gs://<project_bucket>/kaggle_dataset/appearances.csv', header=True, inferSchema=True)
df_club_games = spark.read.csv('gs://<project_bucket>/kaggle_dataset/club_games.csv', header=True, inferSchema=True)
df_clubs = spark.read.csv('gs://<project_bucket>/kaggle_dataset/clubs.csv', header=True, inferSchema=True)
df_games = spark.read.csv('gs://<project_bucket>/kaggle_dataset/games.csv', header=True, inferSchema=True)
df_competitions = spark.read.csv('gs://<project_bucket>/kaggle_dataset/competitions.csv', header=True, inferSchema=True)
df_game_lineups = spark.read.csv('gs://<project_bucket>/kaggle_dataset/game_lineups.csv', header=True, inferSchema=True)
df_player_valuations = spark.read.csv('gs://<project_bucket>/kaggle_dataset/player_valuations.csv', header=True, inferSchema=True)
df_players = spark.read.csv('gs://<project_bucket>/kaggle_dataset/players.csv', header=True, inferSchema=True)
df_transfers = spark.read.csv('gs://<project_bucket>/kaggle_dataset/transfers.csv', header=True, inferSchema=True)



df_competitions_filtered = df_competitions \
    .filter(df_competitions['country_name'].isNotNull()) \
    .dropDuplicates(['name']) \
    .select('competition_id', 'name', 'type', 'country_name', 'confederation', 'is_major_national_league') \
    .withColumnRenamed('name', 'competition_name') \
    .withColumnRenamed('type', 'competition_type')



df_clubs_filtered = df_clubs.join(df_competitions_filtered, df_clubs["domestic_competition_id"] == df_competitions_filtered["competition_id"], how="inner") \
    .select(df_clubs['club_id'], \
            df_clubs['name'].alias('club_name'), \
            df_clubs['domestic_competition_id'], \
            df_clubs['stadium_name'], \
            df_clubs['stadium_seats'])



df_clubs_home = df_clubs_filtered.alias("home_club")
df_clubs_away = df_clubs_filtered.alias("away_club")

df_games_filtered = df_games.join(df_competitions_filtered, df_games["competition_id"] == df_competitions_filtered["competition_id"], how="inner") \
    .join(df_clubs_home, df_games["home_club_id"] == df_clubs_home["club_id"], how="inner") \
    .join(df_clubs_away, df_games["away_club_id"] == df_clubs_away["club_id"], how="inner") \
    .select(df_games['game_id'], \
            df_games['competition_id'], \
            df_games['date'], \
            df_games['season'], \
            df_games['round'], \
            df_games['home_club_id'], \
            df_games['away_club_id'], \
            df_games['home_club_name'], \
            df_games['away_club_name'], \
            df_games['home_club_goals'], \
            df_games['away_club_goals'], \
            df_games['home_club_manager_name'], \
            df_games['away_club_manager_name'], \
            df_games['stadium'], \
            df_games['attendance'], \
            df_games['referee'], \
            df_games['competition_type'])



df_club_games_filtered = df_club_games.join(df_clubs_filtered, df_club_games["club_id"] == df_clubs_filtered["club_id"], how="inner") \
    .join(df_games_filtered, df_club_games["game_id"] == df_games_filtered["game_id"], how="inner") \
    .select(df_club_games['game_id'], \
            df_club_games['club_id'], \
            df_club_games['own_goals'], \
            df_club_games['opponent_id'], \
            df_club_games['opponent_goals'], \
            df_club_games['hosting'], \
            df_club_games['is_win'])



df_players_filtered = df_players \
    .join(df_clubs_filtered, df_players['current_club_id'] == df_clubs_filtered['club_id'], 'inner') \
    .dropDuplicates(['name']) \
    .select(
        df_players['player_id'], 
        df_players['name'].alias('player_name'),  
        df_players['last_season'], 
        df_players['current_club_id'], 
        df_players['country_of_birth'], 
        df_players['country_of_citizenship'].alias('nationality'),  
        df_players['date_of_birth'].cast('date').alias('date_of_birth'),
        (F.datediff(F.current_date(), df_players['date_of_birth'].cast('date')) / 365).cast('int').alias('age'),  
        df_players['position'], 
        df_players['foot'], 
        df_players['height_in_cm'], 
        df_players['market_value_in_eur'], 
        df_players['highest_market_value_in_eur'], 
        df_players['image_url']
    )



df_player_valuations_filtered = df_player_valuations.join(df_players_filtered, df_player_valuations["player_id"] == df_players_filtered["player_id"], how="inner") \
    .join(df_clubs_filtered, df_player_valuations["current_club_id"] == df_clubs_filtered["club_id"], how="inner") \
    .select(df_player_valuations['player_id'], \
            df_player_valuations['date'], \
            F.year(df_player_valuations['date']).alias('season'), \
            df_player_valuations['market_value_in_eur'], \
            df_player_valuations['current_club_id'])


df_game_lineups_filtered = df_game_lineups \
    .filter((df_game_lineups['date'].isNotNull()) & 
            (df_game_lineups['date'] != '0') & 
            (df_game_lineups['date'] != '1')) \
    .join(df_players_filtered, df_game_lineups['player_id'] == df_players_filtered['player_id'], 'inner') \
    .join(df_clubs_filtered, df_game_lineups['club_id'] == df_clubs_filtered['club_id'], 'inner') \
    .join(df_games_filtered, df_game_lineups['game_id'] == df_games_filtered['game_id'], 'inner') \
    .select(
        df_game_lineups['game_lineups_id'],
        df_game_lineups['date'].cast('date').alias('date'),
        df_game_lineups['game_id'],
        df_game_lineups['player_id'],
        df_game_lineups['club_id'],
        df_game_lineups['player_name'],
        df_game_lineups['type'],
        df_game_lineups['position'],
        df_game_lineups['number'],
        df_game_lineups['team_captain']
    )



df_clubs_from = df_clubs_filtered.alias("from_club")
df_clubs_to = df_clubs_filtered.alias("to_club")

df_transfers_filtered = df_transfers \
    .filter(df_transfers['transfer_fee'].isNotNull()) \
    .join(df_clubs_from, df_transfers['from_club_id'] == df_clubs_from['club_id'], 'inner') \
    .join(df_clubs_to, df_transfers['to_club_id'] == df_clubs_to['club_id'], 'inner') \
    .join(df_players_filtered, df_transfers['player_id'] == df_players_filtered['player_id'], 'inner') \
    .select(
        df_transfers['player_id'],
        df_transfers['player_name'],
        df_transfers['transfer_date'],
        (df_transfers['transfer_season'].substr(1, 2).cast('int') + 2000).alias('season'),
        df_transfers['from_club_id'],
        df_transfers['to_club_id'],
        df_transfers['transfer_fee'],
        df_transfers['market_value_in_eur']
    )

df_appearances_filtered = df_appearances \
    .filter(df_appearances['player_name'].isNotNull()) \
    .join(df_competitions_filtered, df_appearances['competition_id'] == df_competitions_filtered['competition_id'], 'inner') \
    .join(df_clubs_filtered, df_appearances['player_club_id'] == df_clubs_filtered['club_id'], 'inner') \
    .join(df_games_filtered, df_appearances['game_id'] == df_games_filtered['game_id'], 'inner') \
    .join(df_players_filtered, df_appearances['player_id'] == df_players_filtered['player_id'], 'inner') \
    .select(df_appearances['*']) 


df_clubs_filtered.write.format('bigquery').option('table', '<project_id>.<dataset_name>.<table_name>').mode('overwrite').save()
df_appearances_filtered.write.format('bigquery').option('table', '<project_id>.<dataset_name>.appearances').mode('overwrite').save()
df_club_games_filtered.write.format('bigquery').option('table', '<project_id>.<dataset_name>.club_games').mode('overwrite').save()
df_games_filtered.write.format('bigquery').option('table', '<project_id>.<dataset_name>.games').mode('overwrite').save()
df_competitions_filtered.write.format('bigquery').option('table', '<project_id>.<dataset_name>.competitions').mode('overwrite').save()
df_game_lineups_filtered.write.format('bigquery').option('table', '<project_id>.<dataset_name>.game_lineups').mode('overwrite').save()
df_player_valuations_filtered.write.format('bigquery').option('table', '<project_id>.<dataset_name>.player_valuations').mode('overwrite').save()
df_players_filtered.write.format('bigquery').option('table', '<project_id>.<dataset_name>.players').mode('overwrite').save()
df_transfers_filtered.write.format('bigquery').option('table', '<project_id>.<dataset_name>.transfers').mode('overwrite').save()
