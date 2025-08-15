from traceback import print_tb

n = int(input())
graph = [[int(1e9) for _ in range(n + 1)] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] =0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]= min(graph[i][j], graph[i][k]+graph[k][j])

m = int(1e9)
for i in graph:
    i[0] =max(i[j] for j in range(1,n+1))
    m = min(m, i[0])
cnt = 0
for i in graph:
    if i[0]== m:
        cnt+=1
print(m, cnt)
check = []
for i in range(1,n+1):
    if graph[i][0] == m:
        check.append(i)

print(*check)
