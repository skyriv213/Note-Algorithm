from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maps = []
for i in range(m):
    maps.append(list(map(int, input().split())))


def bfs(x, y):
    if n == 1 and m == 1:
        return "Yes"

    d = deque([(x, y)])
    dx, dy = [1, 0], [0, 1]

    check = [[False] * n for _ in range(m)]
    check[x][y] = True

    while d:
        x, y = d.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not check[nx][ny] and maps[nx][ny] == 1:
                if nx == m - 1 and ny == n - 1:
                    return "Yes"
                check[nx][ny] = True
                d.append((nx, ny))
    return "No"


res = bfs(0, 0)
print(res)
