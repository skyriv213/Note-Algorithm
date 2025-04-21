'''
1. 문자열의 첫 글자를 읽어서, 이를 기준 문자 x로 정함
2. 왼쪽에서 오른쪽으로 한 글자씩 읽으면서 
    x와 같은 문자이면 x 개수 1 증가
    x가 아닌 다른 문자인 경우 다른 문자 개수 1 증가
3. x 개수와 x가 아닌 자의 개수가 같아지는 순간 지금까지 읽은 부분을 하나의 문자열로 분리 -> answer +=1
4. 분리한 문자열을 빼고 남은 부분에 대해 위과정 반복
    -> 단일 for문으로 그냥 좌에서 우로 진행
5. 더 읽을 부분이 없는데 두 갯수가 다르면 남은 부분을 하나의 문자열로 분리 -> answer +=1

--ps
중복된 문자가 사용될 수 있음
파이썬의 index()는 주어진 문자열에서 가장 가까이 존재하는 인덱스를 반환
'''
from collections import deque
def solution(s):
    answer = 0
    x = s[0]
    temp = deque(s)
    cnt1, cnt2 = 0,0
    while temp:
        t = temp.popleft()
        if x == '':
            x = t
        if t == x:
            cnt1+=1
        else:
            cnt2 +=1
        if cnt1 == cnt2:
            cnt1 = 0
            cnt2 = 0
            x = ''
            answer+=1
    if cnt1 != cnt2:
        answer+=1
    return answer