# 마지막 번호가 나올 수 있어야함
# 주어진 것:
#     num - 번호표
#     stack - 1자형 복도
#     순서대로 나올 수 있어야함
#
# 번호를 체크할 수 있도록 파악 idx
#
# while idx == n:
#     if queue and queue[0] == idx: queue 존재하고 idx와 0번쨰 원소의 값이 동일
#         queue.popleft() ->를 진행하기 위해 queue deque로 변환
#         idx +=1
#     elif stack and stack[-1] == idx:
#         stack.pop()
#         idx +=1
#     else:
#         stack.append(num.popleft())
#     if idx == n:
#         check = True
#

from collections import deque

n = int(input())
queue = deque(map(int, input().split()))
stack = []
idx = 1  # 현재 찾아야 할 번호

while True:
    progress = False
    if queue and queue[0] == idx:
        queue.popleft()
        idx += 1
        progress = True
    elif stack and stack[-1] == idx:
        stack.pop()
        idx += 1
        progress = True
    elif queue:
        stack.append(queue.popleft())
        progress = True

    # 진행 불가 시 루프 종료
    if not progress:
        break
    # 모든 번호 처리 완료
    if idx > n:
        break

print("Nice" if idx == n + 1 else "Sad")
