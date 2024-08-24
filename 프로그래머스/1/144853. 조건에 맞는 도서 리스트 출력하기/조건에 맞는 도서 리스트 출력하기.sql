-- 코드를 입력하세요
SELECT BOOK_ID, Date_Format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from book
where Year(PUBLISHED_DATE) = '2021' and CATEGORY = '인문'
order by 2 asc