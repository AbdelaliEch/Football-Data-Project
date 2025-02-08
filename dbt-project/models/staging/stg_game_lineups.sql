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