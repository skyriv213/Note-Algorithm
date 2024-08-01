# -- 코드를 입력하세요
# SELECT 
# COUNT(IF(AGE IS NULL,USER_ID,NULL)) AS 'USERS' 
# FROM USER_INFO

select count(*)
from USER_INFO
where AGE is NULL