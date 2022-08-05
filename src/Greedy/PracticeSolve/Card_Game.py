n, m = map(int, input().split())

mini = 0

for i in range(n):
    check = list(map(int, input().split()))
    tmp = 1e9
    for j in range(m):
        if check[j] < tmp:
            tmp = check[j]
    if mini < tmp:
        mini = tmp

print(mini)
