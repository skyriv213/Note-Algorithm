-- 코드를 입력하세요
# 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문을 작성해주세요

SELECT 
    u.USER_ID, 
    u.NICKNAME, 
    CONCAT(u.CITY, ' ', u.STREET_ADDRESS1, ' ', u.STREET_ADDRESS2) AS '전체주소',
    ConCat(SubString(u.TLNO,1,3),'-',SubString(u.TLNO,4,4),'-',SubString(u.TLNO,8,4)) as '전화번호'

# select *
from USED_GOODS_USER u
Left join USED_GOODS_BOARD b on b.WRITER_ID=u.USER_ID
group by u.USER_ID
Having Count(u.User_Id) >= 3 
order by u.USER_ID desc