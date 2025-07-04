-- 코드를 입력하세요
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, Date_Format(R.CREATED_DATE, "%Y-%m-%d") as 'CREATED_DATE'
From USED_GOODS_BOARD as B
Join USED_GOODS_REPLY as R on B.BOARD_ID = R.BOARD_ID
where YEAR(B.CREATED_DATE) = "2022" and Month(B.CREATED_DATE) ="10"
Order by 6 asc, 1 asc