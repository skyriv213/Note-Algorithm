def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if cube[x][y] == 0:
        cube[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
cube = [list(map(int, input())) for i in range(n)]

# 얼음의 생성 갯수
cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1

print(cnt)
