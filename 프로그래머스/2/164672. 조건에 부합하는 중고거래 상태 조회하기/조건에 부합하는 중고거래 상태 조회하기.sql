-- 코드를 입력하세요
SELECT u.BOARD_ID	, u.WRITER_ID	,u.TITLE	,u.PRICE	,case
when u.STATUS="SALE" then "판매중"
when u.STATUS="RESERVED" then "예약중"
when u.STATUS="DONE" then "거래완료"
end as "STATUS"
from USED_GOODS_BOARD u
where u.CREATED_DATE = DATE("2022-10-05")
order by 1 desc