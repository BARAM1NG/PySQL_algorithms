with
temp_01 as (
    select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
        , row_number() over (partition by FOOD_TYPE order by FAVORITES desc) as RANKING
    from REST_INFO
)
select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from temp_01
where RANKING = 1
order by FOOD_TYPE desc