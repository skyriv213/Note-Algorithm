'''
각 로프들에 대한 정보가 주어졌을 때,
이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오.
모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.

'''

n = int(input())
l =sorted([int(input()) for _ in range(n)])

dp = [0]*(n)
dp[0] = l[0]*n
for i in range(1,len(l)):
    dp[i] = max(dp[i-1],l[i]*(n-i))
print(max(dp))

