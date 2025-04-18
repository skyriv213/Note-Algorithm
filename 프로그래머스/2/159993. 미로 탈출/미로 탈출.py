'''
각 지점의 인덱스 저장
bfs를 두 번
    ex,ey를 만나면 중지
S에서 - L까지의 최단 거리 = a
L에서 - E까지의 최단 거리 = b
tempMap은 bfs에서 갱신해야함 그래야 s-l에서 생긴 값들이 l-e의 과정에 영향을 안줌
if
    answer = a+b
'''
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start, end, maps):
    sx, sy = start
    ex, ey = end
    
    # 거리 배열 초기화
    tempMap = [[float('inf')] * len(maps[0]) for _ in range(len(maps))]
    tempMap[sx][sy] = 0  # 시작 지점 거리 초기화
    
    q = deque([(sx, sy)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != "X":
                if tempMap[nx][ny] > tempMap[x][y] + 1:
                    tempMap[nx][ny] = tempMap[x][y] + 1
                    q.append((nx, ny))
    
    # 목적지에 도달 불가능한 경우
    if tempMap[ex][ey] == float('inf'):
        return -1
    # 목적지까지의 최단 거리 반환
    return tempMap[ex][ey]

def solution(maps):
    points = {}
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] in ['S', 'L', 'E']:
                points[maps[i][j]] = (i, j)
    
    if 'S' not in points or 'L' not in points or 'E' not in points:
        return -1
    
    # S → L 최단 경로 계산
    time_SL = bfs(points['S'], points['L'], maps)
    if time_SL == -1:
        return -1
    
    # L → E 최단 경로 계산
    time_LE = bfs(points['L'], points['E'], maps)
    if time_LE == -1:
        return -1
    
    return time_SL + time_LE
