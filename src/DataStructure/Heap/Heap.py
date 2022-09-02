'''
우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나다.
우선순위 큐의 경우 우선순위가 가장 높은 데이터를 가장 먼저 삭제한다는 점이 특징이다

스택 - 가장 나중에 삽입된 데이터
큐 - 가장 먼저 삽입된 데이터
우선순위 큐 - 가장 우선순위가 높은 데이터

우선 순위 큐의 경우 데이터를 우선순위에 따라 처리하고 싶을 때 사용
즉 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우

파이썬의 경우 우선순위 큐가 필요할 때 Priority Queue 혹은 heapq를 사용 가능
모두 우선순위 큐 기능 지원, 다만 Priority Queue 보단 heapq가 더 빠르게 동작 → 즉 수행시간 제한된 상황에서는 heapq 사용권장
대부분의 프로그래밍 언어의 경우 첫번째 원소를 기준으로 우선순위를 설정한다.
if 데이터  = (가치, 물건) : 가치의 경우가 우선순위 값이 된다.

우선 순위 큐의 구현은 내부적으로 최소(min)/최대(max)힙을 이용
최소힙 - 값이 낮은 데이터가 먼저 삭제
최대힙 - 값이 큰 데이터가 먼저 삭제

다익스트라 최단 경로 알고리즘의 경우 비용이 적은 노드를 우선 사용 방문으로 최소 힙 구조 기반의
파이썬 우선순위 큐 라이브러리를 사용하면 적합하다.
최소 힙을 최대 힙처럼 사용하기 위해 -의 탈부착으로 값을 돌리는 방식으로 사용하면 된다.


'''