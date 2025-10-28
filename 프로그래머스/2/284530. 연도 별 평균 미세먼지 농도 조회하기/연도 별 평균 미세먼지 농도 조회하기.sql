-- 코드를 작성해주세요
select Year(YM) as 'YEAR', Round(avg(PM_VAL1),2) as 'PM10', Round(avg(PM_VAL2),2) as 'PM2.5'
From AIR_POLLUTION
where LOCATION2 = '수원'
group by YEAR
order by 1 asc