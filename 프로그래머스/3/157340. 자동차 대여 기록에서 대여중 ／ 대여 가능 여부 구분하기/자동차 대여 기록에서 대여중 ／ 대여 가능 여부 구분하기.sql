

SELECT car_id, case
    when Max('2022-10-16' between start_date and end_date) then '대여중'
    else '대여 가능'
    end 'AVAILABILITY'
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
order by 1 desc