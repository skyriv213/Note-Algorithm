from collections import deque

t = int(input())

for _ in range(t):
    n,m = map(int, input().split()) # 문서의 갯수, 몇 번째 문서
    num = list(map(int, input().split())) # 문서의 중요도
    docs = deque([])
    for i in range(n):
        docs.append((num[i],i))
    pri = deque(sorted(num,reverse=True))
    cnt = 0

    while True:
        priority, doc = docs.popleft()
        if priority == pri[0]:
            if doc == m:
                cnt+=1
                break
            cnt+=1
            pri.popleft()
        else:
            docs.append((priority, doc))

    print(cnt)

