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
where club_id is not null