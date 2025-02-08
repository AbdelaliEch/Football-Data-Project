select 
    transfer_season,
    transfer_fee as most_expensive_transfer_fee,
    player_id as most_expensive_transfer_player_id
from 
    {{ ref('stg_transfers') }} as t1
where 
    transfer_fee = (
        select
            max(transfer_fee)
        from
            {{ ref('stg_transfers') }} as t2
        where
            t1.transfer_season = t2.transfer_season
        group by
            transfer_season
    )
and transfer_fee != 0.0