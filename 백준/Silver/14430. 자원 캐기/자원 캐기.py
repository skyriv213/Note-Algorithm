n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        now = area[i][j]
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + now)
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + now)
        if i == 0 and j == 0:
            dp[i][j] = now

print(dp[n - 1][m - 1])
