# 방향
direction = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 1, 1

# 입력값
n = int(input())
check = input().split()

# 계획 확인
for i in check:
    for j in range(4):
        if i == direction[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
