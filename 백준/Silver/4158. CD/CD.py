import sys

input = sys.stdin.readline
while True:

    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break

    answer=0

    cd ={}
    for _ in range(n):
        c = input()
        cd[c] = 1
    for _ in range(m):
        c = input()
        if cd.get(c) == 1:
            answer += 1

    print(answer)

