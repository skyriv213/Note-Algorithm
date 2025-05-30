n = int(input())

if n <=5:
    if n in [2,5]:
        print(1)
    elif n == 4:
        print(2)
    else:
        print(-1)
else:
    dp = [1e9] * (n + 1)
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, n+1):
        dp[i] = min(dp[i-2], dp[i-5])+1
    print(dp[n] if dp[n] != 1e9 else -1)