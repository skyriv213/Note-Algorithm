-- 코드를 작성해주세요

select id, length 
from FISH_INFO
where length is not NULL
order by length desc
limit 10