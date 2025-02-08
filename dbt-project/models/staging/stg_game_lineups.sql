select
    game_lineups_id,
    DATE(date) as date,
    game_id,
    player_id,
    club_id,
    player_name,
    type,
    position,
    number,
    team_captain
from
    {{ source('staging', 'game_lineups') }}
where date is not null and date not in ('0', '1')
and player_id in (
    select player_id from {{ ref('stg_players') }}
) 
and
    club_id in (
        select club_id from {{ ref('stg_clubs') }}
    )
and 
    game_id in (
        select game_id from {{ ref('stg_games') }}
    )