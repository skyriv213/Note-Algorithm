from collections import deque

n, k = map(int, input().split())

num = deque([i for i in range(1, n+1)])
res = []
cnt = 0
while num:
    cnt += 1
    a = num.popleft()

    if cnt == k:
        res.append(a)
        cnt=0
    else:
        num.append(a)

print("<"+", ".join(map(str,res))+">")