select
    cp.club_id,
    cp.season,
    total_games_played,
    total_home_games_played,
    total_away_games_played,
    total_wins,
    total_home_wins,
    total_away_wins,
    home_win_percentage,
    away_win_percentage,
    total_goals_scored,
    total_home_goals_scored,
    total_away_goals_scored,
    total_goals_conceded,
    total_home_goals_conceded,
    total_away_goals_conceded,
    average_goals_per_match,
    average_goals_per_home_match,
    average_goals_per_away_match,
    total_transfers_income,
    total_transfers_spending,
    net_transfer_balance
from
    {{ ref('int_club_performance') }} as cp
join
    {{ ref('int_club_transfers') }} as ct
on 
    cp.club_id = ct.club_id 
and 
    cp.season = ct.season