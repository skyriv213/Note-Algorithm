-- 코드를 입력하세요
SELECT Substring(PRODUCT_CODE,1,2) as CATEGORY,
        count(*) as PRODUCTS
from PRODUCT
Group by CATEGORY
order by CATEGORY