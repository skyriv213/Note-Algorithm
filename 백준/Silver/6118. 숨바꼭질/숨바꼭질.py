# from itertools import combinations
#
# vow = ('a', 'e', 'i', 'o', 'u')
#
# n, m = map(int, input().split())
# s = sorted(list(input().split()))
#
# for p in combinations(s, n):
#     cnt = 0
#     for i in p:
#         if i in vow:
#             cnt += 1
#     if cnt >= 1 and cnt <= n - 2:
#        print(''.join(p))

from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([])
queue.append((1,0))
check =[False]*(n+1)
check[1]= True
res =[]


while queue:
    now, dist = queue.popleft()
    for i in graph[now]:
        if not check[i]:
            queue.append((i, dist+1))
            check[i] = True
            res.append((i, dist+1))


res.sort(key= lambda x: (-x[1],x[0]))
a = res[0][0]
b = res[0][1]
c = 0
for i in res:
    if i[1] == b:
        c+=1

print(a,b,c)
