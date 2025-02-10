select
    game_id,
    club_id,
    own_goals,
    opponent_id,
    opponent_goals,
    hosting,
    is_win
from
    {{ source('staging', 'club_games') }}
where 
    club_id in (
        select club_id from {{ ref('stg_clubs') }}
    )
and 
    game_id in (
        select game_id from {{ ref('stg_games') }}
    )