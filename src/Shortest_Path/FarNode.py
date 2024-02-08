# def dijkstra(start):
#     dist[start]=0
#     visit[start]=True

import heapq


def solution(n, edge):
    maps = [[] for _ in range(n + 1)]
    for i, j in edge:
        # 양방향 그래프
        maps[i].append((j, 1))
        maps[j].append((i, 1))

    dist = [1e9] * (n + 1)

    q = []
    heapq.heappush(q, (0, 1))
    dist[1] = 0

    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for i in maps[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    for i in range(len(dist)):
        if dist[i] == 1e9:
            dist[i] = 0

    return dist.count(max(dist))