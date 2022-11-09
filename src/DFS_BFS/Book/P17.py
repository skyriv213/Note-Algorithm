from collections import deque
from queue import PriorityQueue

'''
경쟁적 감염
'''
n, k = map(int, input().rstrip().split())  # 그래프 크기와 바이러스의 종류
'''
그래프 입력
map 변수를 통해 input으로 입력받은 값들을 int형으로 변환 후 리스트로 변경 및 반복문을 통해 이중리스트 만듬
만들어진 이중리스트는 문제에서 요하는 실험관의 지도
'''
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
s, ox, oy = map(int, input().split())  # 문제에서 요구한 s(시간) / x,y (요구위치)

# 방향이동을 위한 방향표
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 데이터 담을 리스트 선언
data = []

for i in range(0, n):
    for j in range(0, n):
        if graph[i][j] != 0:  # 그래프 탐색에서 그래프의 원소가 0이 아닐경우
            data.append((graph[i][j], i, j, 0))  # 우선순위 큐에 바이러스 종류 , 위치, 그리고 시간초를 체크를 위한 depth를 넣어준다

data.sort()
que = deque(data)

while que:
    vn, x, y, depth = que.popleft()

    if depth == s :
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] != 0:
                continue
            else:
                graph[nx][ny] = vn
                que.append((vn, nx, ny, depth + 1))

print(graph[ox - 1][oy - 1])  # 문제의 답 출력 이 때 그래프의 인덱스는 실제로 0부터이므로 요구위치값에서 -1인 부분을 출력
