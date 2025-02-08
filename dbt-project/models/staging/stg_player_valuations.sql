select 
    player_id,
    date,
    extract(year from date) as season,
    market_value_in_eur,
    current_club_id
from
    {{ source('staging', 'player_valuations') }}