import heapq

def solution(n, k, enemy):
    heap = []
    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])
        n -= enemy[i]
        
        if n < 0:
            if k == 0:
                return i
            max_enemy = -heapq.heappop(heap)
            n+= max_enemy
            k -=1
    return len(enemy)