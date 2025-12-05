import heapq

n, m, x = map(int, input().split()) #x가 목적지
towns = [[] for _ in range(n+1)]
for i in range(m):
    s, e, t = map(int, input().split())
    towns[s].append((e, t))

maxV = 0
# 최단시간에 '왕복' 희망 -> 마을에서도 다익스트라를 진행해야함. 마을 다익스트라는 global로 유지
# 각 마을당 다익스트라 실행 후 왕복의 경우 합산하기

def dijeckstra(idx):
    distance = [int(1e9) for i in range(n+1)]
    hq = []
    heapq.heappush(hq, (0,idx))
    distance[idx] = 0
    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:
            continue
        for next in towns[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(hq, (cost, next[0]))
    return distance


xToTownDistance = dijeckstra(x)

for i in range(1,n+1):
    maxV =  max(maxV,dijeckstra(i)[x] + xToTownDistance[i])

print(maxV)
