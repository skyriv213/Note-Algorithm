t = int(input())
for _ in range(t):
    n = int(input())
    money = list(map(int, input().split()))
    m = int(input())
    memo = [0 for _ in range(m+1)]
    memo[0] = 1
    for coin in money:
        for i in range(coin, m+1):
            memo[i] += memo[i-coin]
    print(memo[m])
    