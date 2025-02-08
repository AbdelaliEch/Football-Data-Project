select
    player_id,
    transfer_date,
    transfer_season,
    from_club_id,
    to_club_id,
    transfer_fee,
    market_value_in_eur
from
    {{ source('staging', 'transfers') }}
where transfer_fee is not null