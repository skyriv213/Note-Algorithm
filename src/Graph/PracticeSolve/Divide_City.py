'''
마을을 두개로 분리
! 최소신장 트리를 하나 만들고 그 사이에 이어진 간선을 하나 제거 ! 이번 문제 핵심 아이디어
최소 신장트리를 만들고 길의 유지비를 최소로 하기 위해서 기존의 최소 신장 트리를 만들고 가장 큰 유지의 간선을 제거한다


'''
def find(city, a):
    if city[a] != a:
        city[a] = find(city, city[a])
    return city[a]


def union(city, a, b):
    a = find(city, a)
    b = find(city, b)
    if a < b:
        city[b] = a
    else:
        city[a] = b


n, m = map(int, input().split())
city = [0] * (n + 1)

# 모든 간선을 담을 리스트
edge = []
result = 0

for i in range(1, n + 1):
    city[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort()
# 최소신장 트리에 포함된 간선 중 가장 비용이 큰 간선
last = 0

for e in edge:
    cost, a, b = e
    if find(city, a) != find(city, b):
        union(city, a, b)
        result += cost
        last = cost

print(result - last)
