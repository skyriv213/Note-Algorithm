t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * (n + 1)
    if n <= 1:
        print(1)
        
    else:
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        print(dp[n])
