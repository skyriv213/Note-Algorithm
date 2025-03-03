'''
n : 페인트를 칠해야하는 구역의 갯수
m : 롤러의 길이
section : 페인트를 다시 칠해야하는 구역

i 지정
만약 i in section
    페인트칠 추가
    i를 다음 구역 체크 할 수 있도록 m만큼 이동
section 내에 없다면
    i+=1
'''

def solution(n, m, section):
    if m == 1:
        return len(section)
    answer = 0
    i=min(section)
    while i<=n:
        if i in section:
            answer+=1
            i+=m
        else:
            i+=1
    return answer