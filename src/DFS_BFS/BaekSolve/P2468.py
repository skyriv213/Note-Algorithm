import sys

# input = sys.stdin.readline

n = int(input())

ground = [list(map(int, input().split())) for i in range(n)]

min = min(min(ground))
max = max(max(ground))

print(ground)
print(min)
print(max)