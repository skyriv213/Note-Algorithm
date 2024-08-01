-- 코드를 입력하세요
SELECT *
from PLACES
where HOST_ID in (
select HOST_ID
from places
    group by host_id
    Having count(host_id) >= 2
)