-- 코드를 작성해주세요
select ID	,EMAIL	,FIRST_NAME, LAST_NAME
from DEVELOPER_INFOS
where SKILL_1 = 'Python' or skill_2 = 'Python' or skill_3 = 'Python'
order by 1 asc