from collections import deque


# def solution(n, computers):
#     answer = 0
#     check =[]

#     def Root(i,n,check):
#         for j in range(n):
#             if computers[i][j]==1 and j not in check:
#                 check.append(j)
#                 Root(j,n,check)

#     for i in range(n):
#         if i not in check:
#             check.append(i)
#             answer +=1
#             Root(i,n,check)

#     return answer

def solution(n, computers):
    answer = 0
    queue = deque([])
    visited = []

    for a in range(n):
        if a not in visited:
            queue.append(a)
            answer += 1
            BFS(computers, n, queue, visited)
    return answer


def BFS(computers, n, queue, visited):
    while queue:
        now = queue.popleft()
        for i in range(n):
            check(computers, i, now, queue, visited)


def check(computers, i, now, queue, visited):
    if computers[now][i] == 1 and i not in visited:
        visited.append(i)
        queue.append(i)



