n = int(input())
p = [list(map(int,input())) for _ in range(n)]


def sol(x, y, n):
    check = p[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != p[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end = '')
        n = n // 2
        sol(x, y, n)
        sol(x, y + n, n)
        sol(x + n, y, n)
        sol(x + n, y + n, n)
        print(")", end = '')

    elif check == 1:
        print(1, end = '')
    else:
        print(0, end = '')


sol(0, 0, n)
