-- 코드를 작성해주세요
SELECT f.ITEM_ID, f.ITEM_NAME	,f.RARITY
FROM ITEM_INFO i
join ITEM_TREE t on i.ITEM_ID = t.PARENT_ITEM_ID
join ITEM_INFO f on f.ITEM_ID = t.ITEM_ID
where i.RARITY = 'RARE'
order by 1 desc