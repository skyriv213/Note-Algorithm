-- 코드를 입력하세요
select ANIMAL_TYPE,
    IFNULL(NAME, "No name") as "NAME",
    SEX_UPON_INTAKE
from ANIMAL_INS
order by ANIMAL_ID