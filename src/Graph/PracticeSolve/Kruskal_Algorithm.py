'''
가장 적은 비용으로 모든 노드 연결 - 그리디 알고리즘으로 분휴

모든 간선에 대하여 정렬 수행 후 가장 거리가 짧은 간선부터 집합에 포함

1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    -1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
    -2. 사이클이 발생하는 경우 최소 신장 트리에 포함 x
3. 모든 간선에 2의 과정 반복

모든 노드가 트리에 포함 되어야하므로 간선의 갯수는 노드의 갯수 -1 이다.

간선의 갯수가 E개일 때, O(ElogE)의 시간 복잡도
크루스칼 알고리즘에서 시간이 가장 오래걸리는 부분이 간선 정렬 작업
E개의 데이터를 정렬했을 때의 시간복잡도는 O(ElogE)이기 때문이다.
크루스칼 내부에서 사용되는 union-find의 경우 시간복잡도가 정렬하는 과정보다 작기에 무시된다.
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for e in edges:
    cost, a, b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
