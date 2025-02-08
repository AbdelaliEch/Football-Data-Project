select 
    prf.player_id,
    player_name,
    prf.year,
    games_played,
    total_yellow_cards,
    total_red_cards,
    total_goals,
    total_assists,
    total_minutes_played,
    goals_per_90_min,
    assists_per_90_min,
    starting_percentage,
    substituting_percentage,
    win_percentage_when_starting,
    win_percentage_when_substitute
from {{ ref('int_player_performance') }} as prf
join
{{ ref('int_player_participation') }} as prt
on 
    prf.player_id = prt.player_id 
and 
    prf.year = prt.year