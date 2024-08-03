-- 코드를 작성해주세요
with priceOfLegend As (
    select PRICE 
    from ITEM_INFO 
    where RARITY = 'LEGEND'
)
select sum(PRICE) as 'TOTAL_PRICE' from priceOfLegend