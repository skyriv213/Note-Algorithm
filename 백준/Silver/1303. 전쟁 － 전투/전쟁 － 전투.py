from collections import deque

# 가로 n, 세로 m
n, m = map(int, input().split())
# 전쟁 입력
war = [list(input()) for _ in range(m)]

# 방향지정 -> 상하좌우
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

answerB, answerW = 0, 0

def bfs(x, y):
    # Queue에 넣고 시작
    color = war[x][y]
    war[x][y] = 0
    cnt = 0
    queue = deque([(x, y)])
    # Queue while
    while queue:
        x, y = queue.popleft()
        cnt += 1
        # for 반복문 4번 방향 체크
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 만약 범위 안, 그리고 동일 색일시 Queue 삽입
            if 0 <= nx < m and 0 <= ny < n:
                if war[nx][ny] == color:
                    queue.append((nx, ny))
                    war[nx][ny] = 0
    return cnt

for i in range(m):
    for j in range(n):
        if war[i][j] == "W":
            answerW += bfs(i, j)**2
        elif war[i][j] == "B":
            answerB += bfs(i, j)**2
print(answerW, answerB)