-- 코드를 입력하세요
SELECT ii.INGREDIENT_TYPE, sum(fh.TOTAL_ORDER) as "TOTAL_ORDER"
from FIRST_HALF as fh
join ICECREAM_INFO as ii on ii.FLAVOR	= fh.FLAVOR	
group by ii.INGREDIENT_TYPE
order by 2 asc