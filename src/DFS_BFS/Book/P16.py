n, m = map(int, input().split())
data = []  # 초기 맵 리스트
temp = [[0] * m for _ in range(n)]  # 벽을 설치한 후 맵의 리스트

# n의 행의 갯수만큼 반복문으로 리스트 입력받기
for _ in range(n):
    data.append(list(map(int, input().split())))

# 이동방향 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0


# DFS 방식 - 각 바이러스가 전체적으로 확산되게 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


# 현재 맵에서 안전 영역 크기 계산
def get_area():
    area = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                area += 1
    return area


# DFS - 울타리 설치 및 안전영역 갱신
def dfs(cnt):
    global result
    # 벽이 3개가 설치된 경우
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                # 벽을 설치한 임시 맵을 원래의 맵으로 초기화
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    # 바이러스 확산
                    virus(i, j)
        # 안전 영역의 최댓값 계산, 기존의 결과값과 비교해서 더 큰 크기의 영역을 반환
        result = max(result, get_area())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            # 각 0인 지점에 벽을 설치하고 DFS 호출
            if data[i][j] == 0:
                data[i][j] = 1
                cnt += 1
                dfs(cnt)
                data[i][j] = 0
                cnt -= 1
