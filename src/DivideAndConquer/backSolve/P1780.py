n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

res = []


def sol(x, y, n):
    check = p[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != p[i][j]:
                n = n // 3
                sol(x, y, n)
                sol(x, y + n, n)
                sol(x, y + (n * 2), n)
                sol(x + n, y, n)
                sol(x + (n * 2), y, n)
                sol(x + n, y + n, n)
                sol(x + (n * 2), y + n, n)
                sol(x + n, y + (n * 2), n)
                sol(x + (n * 2), y + (n * 2), n)
                return

    if check == 1:
        res.append(1)
    elif check == 0:
        res.append(0)
    else:
        res.append(-1)


sol(0, 0, n)
print(res.count(-1))
print(res.count(0))
print(res.count(1))
