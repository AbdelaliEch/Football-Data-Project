select
    season,
    competition_id,
    count(1) as total_games_played,
    sum(home_club_goals + away_club_goals) as total_goals_scored,
    sum(home_club_goals + away_club_goals) / count(1) as average_goals_per_match,
    avg(attendance) as average_attendance
from
    {{ ref('stg_games') }}
group by 
    season, competition_id
order by 
     season, competition_id