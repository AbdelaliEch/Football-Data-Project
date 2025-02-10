select 
    player_id,
    date,
    extract(year from date) as season,
    market_value_in_eur,
    current_club_id
from
    {{ source('staging', 'player_valuations') }}
where 
    player_id in (
        select player_id from {{ ref('stg_players') }}
    ) 
and 
    current_club_id in (
        select club_id from {{ ref('stg_clubs') }}
    )