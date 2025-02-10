select
    player_id,
    player_name,
    transfer_date,
    CAST(LEFT(transfer_season, 2) AS INT) + 2000 AS season,
    from_club_id,
    to_club_id,
    transfer_fee,
    market_value_in_eur
from
    {{ source('staging', 'transfers') }}
where 
    transfer_fee is not null
and 
    from_club_id in (
        select club_id from {{ ref('stg_clubs') }}
    )
and 
    to_club_id in (
        select club_id from {{ ref('stg_clubs') }}
    )
