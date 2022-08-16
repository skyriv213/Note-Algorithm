'''
MST : 최소 신장 트리를 찾기위한 알고리즘
각 노드에서 연결된 간선의 최소치를 찾아 연결
사이클이 생기지 않고 모든 노드가 연결되는것을 목표로 함
다만 이때 간선을 택하는 방식은 그리디 알고리즘의 방법
즉 그 순간에서의 가장 최선의 선택을 하는 것이다.
시간복잡도는 O(E log E), E는 간선의 갯수
우선 순위 큐를 사용해서 구현이 된다.
'''
import heapq

# 노드 수 , 간선 수
n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]  # 그래프 생성
check = [False for _ in range(n + 1)]  # 확인 배열

# 그래프 생성
for _ in range(m):
    u, v, weight = map(int, input().split())
    graph[u].append([weight, u, v]) # 정렬 시 우선순위를 맞춰주기 위해
    graph[v].append([weight, v, u])


def prim(graph, start_node):
    # 시작하는 노드를 True 지나갔다고 체크
    check[start_node] = True
    # 현재 start_node의 행을 그대로 cur 그래프로 생성
    cur = graph[start_node]
    # heapq로 변환, 정렬
    heapq.heapify(cur)
    mst = []  # 최소신장트리
    total = []  # 가중치

    print(cur) # 해당 노드에서는 출발지 1에서의 각 가중치, 출발지, 도착지의 정보를 담고 있다.

    while cur:
        # 저장된 정보를 cur에서 하나씩 뽑아오기, 가중치, 출발지, 도착지
        weight, u, v = heapq.heappop(cur)
        # check[v]가 0이면 진행
        if not check[v]:
            check[v] = True
            print(v)

            # mst에 해당 정보 저장
            mst.append((u, v)) # 출발지, 도착지의 정보를 입력
            total.append(weight)

            # 해당 도착지에서 최소 가중치를 가지는 간선부터 추출, 가중치, 출발지, 도착지 순으로 다음 도착지의 그래프 확인
            for edge in graph[v]:
                if not check[edge[2]]:
                    print("---------")
                    print(edge[2])
                    print(graph[v])
                    print(cur)
                    print(edge[2])
                    print(edge)
                    print("-----------")
                    heapq.heappush(cur, edge)  # 우선 순위 큐에 해당 cur 리스트와 간선을 추가
                    print(cur)
                    print(cur)
    return total, mst

print(prim(graph, 1))
