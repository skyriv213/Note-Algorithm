# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
from collections import deque

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    q =[]
    q.append(start_node)
    visited = []
    while q:
        cur_node = q.pop(0)  # 0번째 원소를 뽑아오겠다는 의미 / 인덱스 기입안할시 뒤에서 뽑아옴

        visited.append(cur_node)
        for i in adj_graph[cur_node]:
            if i not in visited:
                q.append(i)
    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!