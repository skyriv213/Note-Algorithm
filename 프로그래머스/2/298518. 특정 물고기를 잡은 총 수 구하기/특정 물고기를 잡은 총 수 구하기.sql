-- 코드를 작성해주세요
select Count(f.FISH_TYPE) as "FISH_COUNT"
from FISH_INFO f
join FISH_NAME_INFO n on n.FISH_TYPE = f.FISH_TYPE
where n.FISH_NAME in ('BASS','SNAPPER')
