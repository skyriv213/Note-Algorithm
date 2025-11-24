-- 코드를 작성해주세요
with FE as (
    select Sum(CODE) as mask from SKILLCODES where CATEGORY = 'Front End'
),
PY as(
    select CODE from SKILLCODES where NAME = 'Python'
),
CS as(
    select CODE from SKILLCODES where NAME = 'C#'
)

select 
    case
        when (SKILL_CODE & (select mask from FE) and SKILL_CODE &(select Code from PY)) then 'A'
        when SKILL_CODE & (select Code from CS) then 'B'
        when (SKILL_CODE & (select mask from FE)) then 'C'
    END AS 'GRADE',
    ID, EMAIL
from DEVELOPERS
HAVING GRADE IS NOT NULL
ORDER BY GRADE ASC, ID ASC