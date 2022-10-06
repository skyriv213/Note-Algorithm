n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
ans = []


def DFS():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in num:
        if i not in ans:
            ans.append(i)
            DFS()
            ans.pop()

DFS()
