select 
    player_id,
    name as player_name,
    last_season,
    current_club_id,
    country_of_birth,
    DATE(date_of_birth) as date_of_birth,
    DATE_DIFF(CURRENT_DATE(), DATE(date_of_birth), YEAR) AS age,
    position,
    foot,
    height_in_cm,
    market_value_in_eur,
    highest_market_value_in_eur 
from 
    {{ source('staging', 'players') }}
