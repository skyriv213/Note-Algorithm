'''

분리 집합
- 서로소 집합
- 전체집합 U에 대해, U의 분리집합 A,B는 조건을 만족한다
    - A,B는 U의 부분집합
    - A,B는 공통 원소를 가지지 않는다
    - A,B의 합집합이 곧 전체집합 U (A,B에 속하지 않는 U의 원소가 없어야함)
    - 집합의 개수는 더 늘어날 수도 있다.

def find_root(x):
    if x==parent[x] :
        return x
    return find_root(parent[x])

def union_root(x, y):
    x = find_root(x)
    y = find_root(y)

    if x!=y:
        parent[x] ==y

경로 압축(Path Compression)

새로운 간선이 생겼을 때 노드와 노드의 연결을 위해 root 노드를 찾는 경우
연결의 확인을 위해 루트 노드를 탐색하는 경우 root 노드를 재귀를 통해 찾아야한다.

이 때 find 연산을 실행할 때마다 parent[x] = find_root(parent[x])로 지정을 하면
효율적 탐색이 가능해진다

def find_root(x):
    if x==parent[x] :
        return x
    return parent[x] = find_root(parent[x])




'''