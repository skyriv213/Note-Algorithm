def bellman_ford(graph, start):
    # graph는 (u,v,w)의 튜플이며, u에서 v로 가는 가중치 W의 간선을 나타낸다
    # start는 시작 정점

    distance = {vertex: float('infinity') for vertex in graph}
    distance[start] = 0

    # 정점의 수 - 1 만큼 반복
    for _ in range(len(graph) - 1):
        for u, v, w in graph:
            if distance[u] != float('infinity') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # 음수 가중치 사이클 검출
    for u,v, w in graph:
        if distance[u] != float('infinity') and distance[u] +w < distance[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distance


