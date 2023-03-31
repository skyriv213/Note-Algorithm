import sys

n = int(sys.stdin.readline())
p = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

res = []


def sol(x, y, n):
    c = p[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if c != p[i][j]:
                sol(x, y, n // 2)
                sol(x, y + n // 2, n // 2)
                sol(x + n // 2, y, n // 2)
                sol(x + n // 2, y + n // 2, n // 2)
                return
    if c == 0:
        res.append(0)
    else:
        res.append(1)


sol(0, 0, n)
print(res.count(0))
print(res.count(1))
