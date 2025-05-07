a1,a0 = map(int, input().split())
c = int(input())
n0 = int(input())
print(1 if (c >= a1) and (a0 <= (c - a1) * n0) else 0)
