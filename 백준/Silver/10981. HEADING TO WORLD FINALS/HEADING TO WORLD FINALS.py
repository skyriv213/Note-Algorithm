import heapq

n,k = map(int, input().split())

univ = []
for i in range(n):
    a,b,c,d = input().split()
    heapq.heappush(univ,(-1*int(c),int(d),a,b))

seUniv = set()
res = []
while univ and len(res)< k:
    c,d,a,b =heapq.heappop(univ)
    if a not in seUniv:
        seUniv.add(a)
        res.append(b)

for i in res:
    print(i)
