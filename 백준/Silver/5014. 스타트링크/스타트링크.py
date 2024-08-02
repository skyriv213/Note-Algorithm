from collections import deque
import sys

input = sys.stdin.readline

'''
https://www.acmicpc.net/problem/5014
스타트링크
s -> g 최소 몇번을 눌러야하는지 -> 최단거리 -> BFS
f : 총 층수
s : 현재 위치
g : 가고자 하는 위치
u : 올라갈 수 있는 거리 (+)
d : 내려갈 수 있는 거리 (-)
해당 층에 대해 위,아래의 층이 없는 경우 움직이지 않음
엘리베이터로 이동 불가 시 "use the stairs" 출력
'''
f, s, g, u, d = map(int, input().split())

# 이동을 위한 리스트 선언
floor = [1e9 for i in range(1, f + 1)]


# 이동의 경우 u,d만 가능
# 최솟값 출력을 위한 최솟값 정의
# 지나온 층 체크 -> 중복된 층을 이동하는 것은 불가능 -> 무한 루프 가능성
def bfs(f, s, g, u, d):
    # 층별 최소 버튼 클릭 수를 기록할 리스트 초기화
    floor = [int(1e9)] * (f + 1)
    floor[s] = 0

    queue = deque([s])

    while queue:
        cf = queue.popleft()

        # 목표 층에 도달하면 최소 버튼 클릭 횟수 반환
        if cf == g:
            return floor[cf]

        # 다음 가능한 층 계산
        if cf + u <= f and floor[cf + u] == int(1e9):
            floor[cf + u] = floor[cf] + 1
            queue.append(cf + u)

        if cf - d >= 1 and floor[cf - d] == int(1e9):
            floor[cf - d] = floor[cf] + 1
            queue.append(cf - d)

    return "use the stairs"


# BFS 함수 호출 및 결과 출력
result = bfs(f, s, g, u, d)
print(result)
