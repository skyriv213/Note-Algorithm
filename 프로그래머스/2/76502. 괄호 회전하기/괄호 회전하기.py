'''
올바른 문자열의 갯수 카운팅 cnt = 0

deque 사용
왼쪽에서 pop 후 오른쪽으로 append
기본 값은 먼저 ori로 저장
변환된 문자열은 temp로 저장
temp가 ori로 같아지는 순간 반복문 종료 ? ori의 길이만큼만 반복문 시행

해당 문자열 들어올 경우 stack으로 올바른 문자열인지 판별
스택
(,{,[이 들어오면 stack에 저장. 만약에 맞지않는 문자, 혹은 괄호가 존재한다면 false 반환
'''
from collections import deque
def check(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in brackets.values():  # 여는 괄호인지 확인
            stack.append(char)
        elif char in brackets.keys():  # 닫는 괄호인지 확인
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
def solution(s):
    answer = 0
    n = len(s)
    sl = deque(s)
    
    for _ in range(n):
        if check(sl):
            answer += 1
        sl.rotate(-1)  # 왼쪽으로 한 칸 회전
    return answer