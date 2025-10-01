-- 코드를 입력하세요
SELECT CATEGORY, PRICE as 'MAX_PRICE', PRODUCT_NAME
from FOOD_PRODUCT
where (CATEGORY, price) in (
    select category, max(PRICE)
    from FOOD_PRODUCT
    where category in ('과자','국','김치','식용유')
    GROUP BY CATEGORY
)
order by PRICE desc
