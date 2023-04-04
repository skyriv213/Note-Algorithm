import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

s = [0]

for i in range(len(num)):
    s.append(s[i] + num[i])

for _ in range(m):
    a, b = map(int, input().split())
    print(s[b]-s[a-1])

