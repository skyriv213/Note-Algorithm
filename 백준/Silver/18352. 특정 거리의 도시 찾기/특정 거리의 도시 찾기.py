from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입력 전환

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, a = map(int, input().split())

# 도시의 그래프
city = [[] for _ in range(n + 1)]

for _ in range(m):
    i, b = map(int, input().split())
    city[i].append(b)

def bfs(start,k):
    queue = deque([start])
    res = []
    checked = [-1] * (n + 1)
    checked[start] = 0
    while queue:
        c = queue.popleft()
        for i in city[c]:
            if checked[i] == -1:
                checked[i] = checked[c] + 1
                queue.append(i)
                if checked[i] == k:
                    res.append(i)
    return res

res = bfs(a,k)
res.sort()
if not res:
    print(-1)
else:
    print('\n'.join(map(str, res)))