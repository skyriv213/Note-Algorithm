n =  int(input())
num = list(map(int, input().split()))

memo = [0] * (n)
for i in range(n):
    for j in range(i):
        if num[i] < num[j] and memo[i] < memo[j]:
            memo[i] = memo[j]
    memo[i]+=1
print(max(memo))
