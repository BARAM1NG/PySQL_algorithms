select T.ITEM_ID, I.ITEM_NAME, I.RARITY
from ITEM_INFO I
join ITEM_TREE T on I.ITEM_ID = T.ITEM_ID
where PARENT_ITEM_ID in (
    select ITEM_ID
    from ITEM_INFO
    where RARITY = 'RARE'
)
order by ITEM_ID desc;