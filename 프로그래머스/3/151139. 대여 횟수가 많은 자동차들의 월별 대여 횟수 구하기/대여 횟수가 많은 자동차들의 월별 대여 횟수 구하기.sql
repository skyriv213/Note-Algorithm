-- 코드를 입력하세요
SELECT Month(C.START_DATE) as 'MONTH', C.CAR_ID, Count(*) as RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY as C
Where START_DATE Between "2022-08-01" and "2022-10-31" and Car_Id in (
select Car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where START_DATE Between "2022-08-01" and "2022-10-31"
group by car_id
having Count(*) >=5)
Group by Month, car_id
order by month asc, car_id desc