select 
    club_id,
    name as club_name,
    domestic_competition_id,
    stadium_name,
    stadium_seats, 
from 
    {{ source('staging', 'clubs') }}