'''
벽의 갯수는 3개, 꼭 3개를 세워야함
0은 빈칸, 1은 벽, 2는 바이러스
벽이 3개 세워지면 (cnt ==3)
- 2를 퍼지도록 설계 -> 2가 다 퍼지면
    - 0의 갯수 확인하기
- max의 값을 저장하고 벽이 3개 세워질때마다 max의 갯수를 갱신

DFS로 진행
- 벽을 세우는 기준
- 해당 벽을 세운 기록이 있는가?
    - check를 통해 검사?
    - 0을 만나면 벽을 세운다

'''
import copy
from collections import deque
n, m = map(int, input().split())
labor = [list(map(int, input().split())) for _ in range(n)]
maxV = 0

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs_virus(temp):
    queue = deque([])
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if temp[i][j] == 2:
                queue.append((i,j))

    while queue:
        r, c = queue.popleft()

        for i, j in direct:
            nr = r + i
            nc = c + j
            if 0 <= nr < n and 0 <= nc < m and temp[nr][nc] == 0:
                temp[nr][nc] = 2
                queue.append((nr, nc))

def count(temp):
    area = 0
    for i in temp:
        for j in i:
            if j == 0:
                area += 1
    return area


def dfs(cnt):
    global maxV
    if cnt == 3:
        tempMap = copy.deepcopy(labor)
        bfs_virus(tempMap)
        maxV = max(maxV, count(tempMap))
        return

    for i in range(len(labor)):
        for j in range(len(labor[0])):
            if labor[i][j] == 0:
                labor[i][j] = 1
                dfs(cnt + 1)
                labor[i][j] = 0


dfs(0)
print(maxV)
