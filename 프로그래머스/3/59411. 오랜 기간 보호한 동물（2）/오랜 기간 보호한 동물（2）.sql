-- 코드를 입력하세요
SELECT o.ANIMAL_ID	, o.NAME
from ANIMAL_OUTS as o
join ANIMAL_INS as i on o.ANIMAL_ID = i.ANIMAL_ID

order by DateDiff(o.DATETIME, i.DATETIME) desc
limit 2