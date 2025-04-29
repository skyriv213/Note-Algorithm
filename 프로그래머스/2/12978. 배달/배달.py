# from collections import deque

import heapq
'''
마을 갯수: N
a,b,c = a <-> b = c
음식 배달이 가능한 시간 <= k

town 생성
town[a].append((b,c))
town[b].append((a,c))

최단거리이므로 BFS
시작을 기준으로 방문 체크 진행
갈 수 있는 마을의 방문을 다 했으면 while 조건에 의해 탈출

출력
sum(1 for i in time if i<=K)

'''
def solution(N, road, K):
    town = [[] for _ in range(N+1)]
    time = [1e9] *(N+1)
    
    for a,b,c in road:
        town[a].append((b,c))
        town[b].append((a,c))
    
    def dijkstra():
        q = []
        heapq.heappush(q, (0,1))
        time[1] =0
        while q:
            dist, now = heapq.heappop(q)
            if time[now]< dist:
                continue
                
            for t, c in town[now]:
                cost = dist + c
                if cost < time[t]:
                    time[t] = cost
                    heapq.heappush(q,(cost,t))

            
    dijkstra()

    return sum(1 for i in time if i<=K)