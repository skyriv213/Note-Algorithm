-- 코드를 입력하세요
SELECT
 MCDP_CD as '진료과코드',
 count(APNT_NO) as '5월예약건수'
from APPOINTMENT
where MONTH(APNT_YMD) = '05' and year(APNT_YMD) = '2022'
group by 1
order by 2 asc, 1 asc