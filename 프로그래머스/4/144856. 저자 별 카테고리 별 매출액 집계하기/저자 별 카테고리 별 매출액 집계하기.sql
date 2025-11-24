-- 코드를 입력하세요
SELECT b.AUTHOR_ID, a.AUTHOR_NAME	, b.CATEGORY, sum(b.PRICE* bb.SALES) as 'TOTAL_SALES'
from BOOK as b
join AUTHOR a on a.AUTHOR_ID = b.AUTHOR_ID
join BOOK_SALES bb on bb.BOOK_ID = b.BOOK_ID
where Year(bb.SALES_DATE) = '2022' and Month(bb.SALES_DATE) ='01'
group by b.AUTHOR_ID, a.AUTHOR_NAME	, b.CATEGORY
order by b.AUTHOR_ID asc,  b.CATEGORY desc