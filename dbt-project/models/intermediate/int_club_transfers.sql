with income as (
    select 
        transfer_season,
        CAST(LEFT(transfer_season, 2) AS INT) + 2000 AS season,
        from_club_id as club_id,
        sum(transfer_fee) as total_transfers_income
    from 
        {{ ref('stg_transfers') }}
    group by
        transfer_season, from_club_id
),
spending as (
    select
        transfer_season,
        to_club_id as club_id,
        sum(transfer_fee) as total_transfers_spending
    from 
        {{ ref('stg_transfers') }}
    group by
        transfer_season, to_club_id
)
select 
    season,
    income.club_id,
    total_transfers_income,
    total_transfers_spending,
    (total_transfers_income - total_transfers_spending) as net_transfer_balance
from 
    income 
join 
    spending
on
    income.club_id = spending.club_id and income.transfer_season=spending.transfer_season