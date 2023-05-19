import heapq
import sys

input = sys.stdin.readline

n = int(input())
card = []

for _ in range(n):
    heapq.heappush(card, int(input()))

ans = 0

if len(card) == 1:
    print(0)
else:
    while len(card)>1:
        p = heapq.heappop(card) + heapq.heappop(card)
        ans += p
        heapq.heappush(card,p)

print(ans)