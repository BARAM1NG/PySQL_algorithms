-- 코드를 입력하세요
select
    A.AUTHOR_ID,
    A.AUTHOR_NAME,
    B.CATEGORY,
    sum(BS.SALES * B.PRICE) as TOTAL_SALES
from BOOK B
join AUTHOR A on B.AUTHOR_ID = A.AUTHOR_ID
join BOOK_SALES BS on B.BOOK_ID = BS.BOOK_ID
where BS.SALES_DATE like '2022-01%'
group by A.AUTHOR_ID, B.CATEGORY
order by A.AUTHOR_ID asc, B.CATEGORY desc;