-- 코드를 작성해주세요

# ifnull - null 확인 자리, null값이라면 대체할 값 체크
# AVG() - 해당 열들에 대한 평균 도출
# Round() - 반올림(인자, 몇번째 자리까지 표시할 것인지)
# CEIL() - 소숫점 올림 처리
# FLOOR() - 소숫점 버림 처리

select Round(avg(ifnull(Length,10)),2) as 'AVERAGE_LENGTH'
from FISH_INFO
