-- 코드를 작성해주세요
select hr.DEPT_ID, hr.DEPT_NAME_EN, round(avg(he.sal)) as 'AVG_SAL'
from HR_DEPARTMENT as hr
join HR_EMPLOYEES as he on hr.DEPT_ID = he.DEPT_ID
group by DEPT_ID, DEPT_NAME_EN
order by 3 desc