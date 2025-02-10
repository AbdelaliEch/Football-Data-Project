with duplicates as (
    select 
        ROW_NUMBER() OVER(PARTITION BY name ORDER BY highest_market_value_in_eur DESC) AS rank,
        player_id,
        name as player_name,
        last_season,
        current_club_id,
        country_of_birth,
        country_of_citizenship as nationality,
        DATE(date_of_birth) as date_of_birth,
        DATE_DIFF(CURRENT_DATE(), DATE(date_of_birth), YEAR) AS age,
        position,
        foot,
        height_in_cm,
        market_value_in_eur,
        highest_market_value_in_eur,
        image_url
    from 
        {{ source('staging', 'players') }}
)
select * from duplicates where rank=1
and 
    current_club_id in (
        select club_id from {{ ref('stg_clubs') }}
    )
