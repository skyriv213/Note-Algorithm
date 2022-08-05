# 이동 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 맵의 크기, 캐릭터 존재 좌표, 바라보는 방향 입력
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 맵 입력받기
world = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * m for _ in range(n)]

# 방문 처리
d[x][y] = 1

# 초기 방문한 칸, 회전의 수
cnt, turn_time = 1, 0

# 방향 회전
# 주어진 direction에서 1씩 감소하면서 3이 되었을 경우 서쪽을 바라본 시점

def turn():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

while True:
    turn()
    nx, ny = x + dx[direction], y + dy[direction]
    if d[nx][ny] == 0 and world[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx, ny = x - dx[direction], y - dy[direction]

        if world[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(cnt)
