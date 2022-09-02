import sys

input = sys.stdin.readline
INF = int(1e9)

# 그래프 및 방문 확인 / 거리
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    a, b, c = map(int, input())
    graph[a].append((b, c))

#-----------------------------------------------------------------------------------------------------------------------
'''
시간 복잡도가 O(v^2)인 방법이다. 총 o(v)에 걸쳐 최단거리가 가장 짧은 노드를 매번 선형 탐색, 매번 일일이 확인
구형 방법, 실전에서는 뒤에 나오는 방법 사용
'''
# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra01(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = 0
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 논드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] == True
        # 현재 노드와 연결이 된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

#-----------------------------------------------------------------------------------------------------------------------
'''
시간 복잡도는 O(ElogV) v는 노드의 개수, e는 간선의 개수
개선된 다익스트라 알고리즘의 경우 힙 자료 구조 사용.
특정 노드 까지의 최단 거리에 대한 정보를 힙에 담아 출력 → 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾음
'''


#-----------------------------------------------------------------------------------------------------------------------
dijkstra01(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
   # 도달할 수 없는 경우, 무한(INF) 출력
    if distance[i] == INF:
        print("Inf")
    # 도달할 수 없는 경우 거리를 출력
    else:
        print(distance[i])