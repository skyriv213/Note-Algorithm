from itertools import count

n, m = map(int, input().split())
friend = [[int(1e9)] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a][b] = 1
    friend[b][a] = 1
for i in range(1,n+1):
    friend[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            friend[i][j] = min(friend[i][j], friend[i][k]+friend[k][j])


ans, temp = 0, 1e9
for i, v in enumerate(friend):
    if temp > sum(v[1:]):
        ans = i
        temp = sum(v[1:])

print(ans)
