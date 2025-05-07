n = int(input())
num = list(map(int, input().split()))
if n == 1:
    print(num[0])
    exit()
dp= num.copy()

for i in range(n):
    for j in range(i):
        if  num[j] < num[i]:
            dp[i]= max(dp[i], dp[j]+num[i]) # 합이기에 원소를 더함
print(max(dp))
