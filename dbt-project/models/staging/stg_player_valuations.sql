select 
    player_id,
    date,
    market_value_in_eur,
    current_club_id
from
    {{ source('staging', 'player_valuations') }}