-- 코드를 입력하세요
select
    A.WRITER_ID,
    B.NICKNAME,
    concat(B.CITY, " ", B.STREET_ADDRESS1, " ", B.STREET_ADDRESS2) as "전체주소",
    CONCAT(SUBSTRING(TLNO, 1, 3), '-', 
              SUBSTRING(TLNO, 4, 4), '-', 
              SUBSTRING(TLNO, 8, 4)) as '전화번호'
from USED_GOODS_BOARD A
join USED_GOODS_USER B on A.WRITER_ID = B.USER_ID
group by A.WRITER_ID
having COUNT(BOARD_ID) >= 3
order by A.WRITER_ID DESC;
