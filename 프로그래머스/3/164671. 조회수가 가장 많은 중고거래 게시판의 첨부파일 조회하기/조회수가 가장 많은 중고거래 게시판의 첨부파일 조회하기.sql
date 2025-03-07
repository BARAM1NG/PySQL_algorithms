select concat('/home/grep/src/', F.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME, F.FILE_EXT) as 'FILE_PATH'
from USED_GOODS_BOARD B
join USED_GOODS_FILE F on B.BOARD_ID = F.BOARD_ID
where VIEWS = (select max(VIEWS) from USED_GOODS_BOARD)
order by F.FILE_ID desc