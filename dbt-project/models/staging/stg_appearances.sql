select 
    * 
from 
    {{ source('staging', 'appearances') }}
where 
    player_name is not null 
and 
    competition_id in (
        select competition_id from {{ ref('stg_competitions') }}
    )
and 
    player_club_id in (
        select club_id from {{ ref('stg_clubs') }}
    )
and 
    game_id in (
        select game_id from {{ ref('stg_games') }}
    )
and
    player_id in (
        select player_id from {{ ref('stg_players') }}
    ) 