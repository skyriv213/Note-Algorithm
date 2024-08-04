
import sys
from collections import deque

input = sys.stdin.readline

# 그래프 입력
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))


def bfs(n, m):
    # 벽 뚥기 전 0 , 뚫은 후 1 체크를 위한 3차원 배열 선언
    check = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    q = deque([(0, 0, 0)])
    check[0][0][0] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y, wb = q.popleft()
        # 도착하는 경우 발생 시 함수의 종료
        if x == n - 1 and y == m - 1:
            return check[x][y][wb]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 위치가 그래프의 크기를 벗어나는지 확인
            if 0 <= nx < n and 0 <= ny < m:
                # wb는 벽을 뚫었는지 안뚫었는지 체크용
                # 다음 칸은 이전 칸 +1
                if graph[nx][ny] == 0 and check[nx][ny][wb] == 0:
                    check[nx][ny][wb] = check[x][y][wb] + 1
                    q.append((nx, ny, wb))
                # 해당 위치가 벽인지 확인, 현재 경로를 진행하면서 벽을 부순 경우가 존재하는지 확인
                elif graph[nx][ny] == 1 and wb == 0:
                    check[nx][ny][1] = check[x][y][0] + 1
                    q.append((nx, ny, 1))

    return -1


res = bfs(n, m)
print(res)
