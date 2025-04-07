from collections import deque

n = int(input())
jump = [0]+list(map(int, input().split()))
start, end = map(int, input().split())


def bfs(start, end):
    queue = deque([start])
    check = [-1] * (n + 1)
    check[start] = 0
    while queue:
        now = queue.popleft()
        for i in range(now, n + 1, jump[now]):
            if check[i] == -1:
                queue.append(i)
                check[i] = check[now] + 1
                if i == end:
                    return check[i]
        for i in range(now, 0, -jump[now]):
            if check[i] == -1:
                queue.append(i)
                check[i] = check[now] + 1
                if i == end:
                    return check[i]
    return -1


print(bfs(start, end))
