-- 코드를 작성해주세요

Select d.ID, d.EMAIl, d.FIRST_NAME, d.LAST_NAME
from DEVELOPERS d
join SKILLCODES s on s.CODE & d.SKILL_CODE != 0
where s.NAME in ("Python","C#")
group by     D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME

order by 1 asc