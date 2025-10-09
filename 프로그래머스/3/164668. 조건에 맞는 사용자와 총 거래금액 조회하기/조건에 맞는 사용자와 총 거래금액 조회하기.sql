-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, Sum(g.PRICE) as 'TOTAL_SALES'
From USED_GOODS_USER u
join USED_GOODS_BOARD g on u.USER_ID = g.WRITER_ID
where g.STATUS = 'DONE' 
group by g.WRITER_ID
having TOTAL_SALES>=700000
order by TOTAL_SALES asc