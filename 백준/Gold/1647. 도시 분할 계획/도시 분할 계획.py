
'''
도시 분할 계획
크루스칼 알고리즘
-> 사이클이 존재하지 않는 두개의 최소 신장 트리
-> 하나의 최소 신장 트리 생성 후 가장 비용이 큰 간선 하나 제거
'''

def find(town, x):
    if town[x] != x:
        town[x] = find(town, town[x])
    return town[x]


def union(town, a, b):
    a = find(town, a)
    b = find(town, b)
    if a < b:
        town[b] = a
    else:
        town[a] = b


n, m = map(int, input().split())  # n개의 집과 그 집들을 연결하는 m개의 길
town = [0] * (n + 1)
edges =[]

for i in range(1, n + 1):
    town[i] = i

for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()

res = 0
maxCost = 0
for e in edges:
    c,a,b = e
    if find(town, a) != find(town,b):
        union(town, a,b)
        res+=c
        maxCost = max(maxCost,c)

print(res - maxCost)
