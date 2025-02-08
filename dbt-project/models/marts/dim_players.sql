select 
    prf.season,
    prf.player_id,
    player_name,
    games_played,
    total_minutes_played,
    total_goals,
    total_assists,
    total_yellow_cards,
    total_red_cards,
    ROUND(goals_per_90_min, 3) as goals_per_90_min,
    ROUND(assists_per_90_min, 3) as assists_per_90_min,
    ROUND(starting_percentage, 3) as starting_percentage,
    ROUND(substituting_percentage, 3) as substitute_percentage,
    ROUND(win_percentage_when_starting, 3) as win_percentage_when_starting,
    ROUND(win_percentage_when_substitute, 3) as win_percentage_when_substitute
from {{ ref('int_player_performance') }} as prf
join
    {{ ref('int_player_participation') }} as prt
on 
    prf.player_id = prt.player_id 
and 
    prf.season = prt.season
join
    {{ ref('int_player_market_value') }} as pmv 
on
    prf.player_id = pmv.player_id
and
    prf.season = pmv.season
order by season desc