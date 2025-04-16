'''
상자는 번호 증가 순으로 1-n 컨테이너 벨트 존재

1번 순서대로 상자 내리기 가능 -> Queue -> deque로 사용
보조 컨테이너 벨트 마지막 들어온 상자부터 내리기 가능 -> Stack -> 리스트 사용



'''
from collections import deque

def solution(order):
    answer = 0
    stack = []
    queue = deque(range(1, len(order) + 1))  # 1번부터 n번까지

    idx = 0  # order에서 내릴 차례의 인덱스

    while queue or stack:
        if queue and queue[0] == order[idx]:
            queue.popleft()
            answer += 1
            idx += 1
        elif stack and stack[-1] == order[idx]:
            stack.pop()
            answer += 1
            idx += 1
        elif queue:
            stack.append(queue.popleft())
        else:
            break  

        if idx == len(order):
            break

    return answer