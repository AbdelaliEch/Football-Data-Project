select 
    player_name,
    count(1) as games_played,
    sum(yellow_cards) as total_yellow_cards,
    sum(red_cards) as total_red_cards,
    sum(goals) as total_goals,
    sum(assists) as total_assists,
    sum(minutes_played) as total_minutes_played,
    extract(year from date) as year
from 
    {{ ref('stg_appearances') }}
group by 
    player_name, year
order by 
    player_name, year