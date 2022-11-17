from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
for _ in range(m):
    # a에서 b까지의 도로가 존재
    a, b = map(int, input().split())
    graph[a].append(b)

# 주어진 도시를 기준으로 정렬
distance = [-1] * (n + 1)
distance[x] = 0


# BFS로 접근
# deque에 원소 추가
q = deque([x])
while q:
    now = q.popleft()
    # 반복문 순회
    for nn in graph[now]:
        # 기존의 값이 0이면 한번도 지나가지않은 도시
        if distance[nn] == -1:
            # now 도시를 거쳐서 도시로 온것이므로 now 거리 값에 +1을 해준다
            distance[nn] = distance[now] + 1
            q.append(nn)

# 만약 반복문을 통해 거리의 값이 k인 도시가 존재한다면 s 문자열에 join 메서드로 추가
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
if not check:
    print(-1)

# # 만약 s의 값이 ' '랑 동일하다면 해당 -1값을 출력 → 시간 초과
# if s == ' ':
#     print(-1)
# else:
#     print(s)


