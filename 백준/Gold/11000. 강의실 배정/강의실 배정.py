import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())

classRoom = [list(map(int, input().split())) for _ in range(n)]
classRoom.sort(key=lambda x: x[0])

heapClass = []
heapq.heappush(heapClass, classRoom[0][1])

for i in range(1, n):
    if heapClass[0] <= classRoom[i][0]:
        heapq.heappop(heapClass)
    heapq.heappush(heapClass, classRoom[i][1])

print(len(heapClass))
