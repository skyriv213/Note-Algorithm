n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
ans = []


def DFS(start):
    # ans 출력을 통해 답안 출력
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(start, n):
        ans.append(num[i])
        DFS(i)
        ans.remove(num[i])


DFS(0)
