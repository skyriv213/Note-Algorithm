'''
설탕 배달
설탕은 3, 5로 존재
최대한 적은 봉지
N이 주어지며 3 ~ 5000 사이
'''
n = int(input())
dp = [int(1e9)] * (n+5)

if n >= 3:
    dp[3] = 1
if n >= 5:
    dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-3], dp[i-5])+1

print(dp[n] if dp[n] < int(1e9) else -1)
