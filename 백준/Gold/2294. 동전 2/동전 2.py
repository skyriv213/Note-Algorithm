n,m = map(int,input().split())
coin = [int(input()) for _ in range(n)]

dp = [10001] * (m+1)

dp[0]= 0



for i in range(1, m+1):
    for j in coin:
        if i>=j:
            dp[i] = min(dp[i], dp[i-j]+1)

print(dp[m] if dp[m]!=10001 else -1)



