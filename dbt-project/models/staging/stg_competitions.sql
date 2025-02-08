select 
    competition_id,
    name as competition_name,
    type as competition_type,
    country_name,
    confederation,
    is_major_national_league
from 
    {{ source('staging', 'competitions') }}
where country_name is not null