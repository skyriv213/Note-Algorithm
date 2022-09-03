'''
정렬 알고리즘의 일종
순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'

진입차수 : 특정한 노드로 들어오는 간선의 개수

1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌때까지 다음 과정 반복
    -1 : 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
    -2 : 새롭게 진입차수가 0이 된 노드를 큐에 삽입

만약 모든 원소를 방문하기 전 큐가 빈다면 사이클이 존재한다고 판정
사이클이 존재하는 경우 사이클에 포함되어 있는 원소 중에서 어떠한 원소도 큐애 들어가지 못하기 때문
위상 정렬 문제에서 사이클이 존재하지 않는다고 명시하는 경우가 더 많음

위상정열릐 시간복잡도는 O(V + E)
위상 정렬을 수행할 때는 차례대로 모든 노드를 확인하면서 해당 노드에서 출발하는 간선을 차례대로 제거
노드와 간선을 모두 확인하는 측면에서 O(v+e)의 시간이 소요
'''

from collections import deque

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수를 1 증가
    indegree[b] += 1


# 위상정렬 함수
def topology_sort():
    result = []
    q = deque()

    # 처음 시작할 때 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
       if indegree[i] ==0:
           q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼주기
        for i in graph[now]:
            indegree[i] -=1
            # 새롭게 진입차수가 0인 i를 큐에 넣어주기
            if indegree[i]==0:
                q.append(i)

    # 위상정렬 수행결과 출력
    for i in result:
        print(i, end = " ")

topology_sort()
