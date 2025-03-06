-- 2021년에 가입한 전체 회원
-- 구매한 회원수 & 구매한 회원의 비율(소수점 두번째자리에서 반올림)
-- 년, 열 별로 출력
with
temp_01 as (
    select *
    from USER_INFO
    where YEAR(JOINED) = 2021
),
temp_02 as (
    select count(*) as TOTAL_CNT
    from temp_01
)
select YEAR(a.SALES_DATE) as YEAR
    , MONTH(a.SALES_DATE) as MONTH
    , count(distinct a.USER_ID) as PURCHASED_USERS
    , round(count(distinct a.USER_ID) / (select TOTAL_CNT from temp_02), 1) as PUCHASED_RATIO
from ONLINE_SALE a
    join temp_01 b on a.USER_ID = b.USER_ID 
group by YEAR(a.SALES_DATE), MONTH(a.SALES_DATE)
order by 1, 2;