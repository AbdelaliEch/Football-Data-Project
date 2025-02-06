select 
    * 
from 
    {{ source('staging', 'appearances') }}
where 
    player_name is not null 