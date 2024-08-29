-- 코드를 입력하세요
SELECT MEMBER_ID	, MEMBER_NAME, GENDER	, DATE_Format(DATE_OF_BIRTH,"%Y-%m-%d") as 'DATE_OF_BIRTH
'
from MEMBER_PROFILE
where TLNO	is not null and Month(DATE_OF_BIRTH) = '03' and GENDER='W'
order by 1