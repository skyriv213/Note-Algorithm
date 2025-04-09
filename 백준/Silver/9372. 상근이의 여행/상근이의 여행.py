import sys

input = sys.stdin.readline

'''
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5


'''
def graph(node, cnt):
    check[node] = True
    for i in travel[node]:
        if not check[i] :
            cnt = graph(i, cnt + 1)

    return cnt

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    travel = [[] for _ in range(n+1)]
    check = [False] *(n+1)
    for _ in range(m):
        a,b = map(int, input().split())
        travel[a].append(b)
        travel[b].append(a)
    print(graph(1, 0))

