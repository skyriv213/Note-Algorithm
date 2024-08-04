-- 코드를 작성해주세요
select count(ID) as 'FISH_COUNT'
from FISH_INFO
group by LENGTH
having LENGTH is null