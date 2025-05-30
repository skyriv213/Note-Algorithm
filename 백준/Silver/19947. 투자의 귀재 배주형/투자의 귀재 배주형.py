h, y = map(int, input().split())
dp = [0] * (y + 1)
dp[0] = h

for i in range(1, y + 1):
    max_val = int(dp[i - 1] * 1.05)  # 기본: 1년 복리
    if i >= 3:
        max_val = max(max_val, int(dp[i - 3] * 1.2))
    if i >= 5:
        max_val = max(max_val, int(dp[i - 5] * 1.35))
    dp[i] = max_val

print(dp[y])
