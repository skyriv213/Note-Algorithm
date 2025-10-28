-- 코드를 입력하세요
SELECT distinct(c.CAR_ID)
From CAR_RENTAL_COMPANY_CAR c
join CAR_RENTAL_COMPANY_RENTAL_HISTORY r on c.CAR_ID = r.CAR_ID
where CAR_TYPE = '세단' and Month(r.START_DATE) = 10 
order by c.Car_id desc
