n = int(input())
classRoom = []
tempRoom = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(n):
    classRoom.append(list(input().split()))

def checkStudent(tempRoom, x, y):
    # 상하좌우 탐색
    for d in range(4):
        nx, ny = x, y
        while 0 <= nx < n and 0 <= ny < n:
            if tempRoom[nx][ny] == "O":  # 장애물을 만나면 감시 종료
                break
            if tempRoom[nx][ny] == "S":  # 학생을 만나면 실패
                return False
            nx += dx[d]
            ny += dy[d]
    return True

def safe():
    for i in range(n):
        for j in range(n):
            if tempRoom[i][j] == "T":  # 선생님 위치에서 감시
                if not checkStudent(tempRoom, i, j):
                    return "NO"
    return "YES"

def dfs(count):
    if count == 3:  # 장애물을 3개 설치했을 때
        for i in range(n):
            for j in range(n):
                tempRoom[i][j] = classRoom[i][j]
        
        if safe() == "YES":
            print("YES")
            exit()  # 즉시 종료 (찾으면 더 이상 탐색할 필요 없음)
        return
    
    for i in range(n):
        for j in range(n):
            if classRoom[i][j] == "X":  # 빈 공간에 장애물 설치
                classRoom[i][j] = "O"
                dfs(count + 1)
                classRoom[i][j] = "X"  # 백트래킹 (다시 원래대로 복구)

dfs(0)
print("NO")  # 끝까지 탐색해도 "YES"가 안 나오면 "NO"
