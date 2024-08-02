from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

com = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    com[b].append(a)

number = [0]

def bfs(start):
    cnt = 1
    dq = deque([start])
    check = [False] * (n + 1)
    check[start] = True
    while dq:
        a = dq.pop()
        for i in com[a]:
            if not check[i]:
                dq.append(i)
                check[i] = True
                cnt += 1
    return cnt

res=[]
max_cnt = 1
for i in range(1, n + 1): 
	cnt = bfs(i)
	if cnt > max_cnt:
		max_cnt = cnt
		res = []
		res.append(i)
	elif cnt == max_cnt:
		res.append(i)

print(*res)
