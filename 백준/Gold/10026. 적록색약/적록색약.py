from collections import deque

'''
1. 기본적인 컬러별 구역 조회
- 구역이 달라지는 경우 cnt+=1
2. 색맹의 경우 컬러별 구역 조회
- R,G / B를 기준으로 구역 조회, 구역이 달라지는 경우 cnt+=1

조회 방법
- BFS 사용

구현방법
1. n 입력
2. pic 입력
3. 기본 컬러 구역
- check 구현
- for 반복문 사용
    - 만약 check가 False라면 BFS 실행
    - BFS 실행 시 해당 색상을 변수로 삽입
    - 한번의 BFS가 끝날때마다 CNT 증가
    
4. 색맹 컬러 구역
- check 구현
- for 반복문 사용
    - 만약 check가 False라면 BFS 실행
    - B,R의 경우 하나의 구역으로 판단 -> BFS를 개별적으로 구현해야할듯
    - 한번의 BFS가 끝날때마다 CNT 증가

'''

n = int(input())

pic = [list(input()) for _ in range(n)]

def bfs(check,pic, colorG,i,j):
    dxy = [(0,1),(1,0),(-1,0),(0,-1)]
    q = deque([(i, j)])
    check[i][j] = True
    while q:
        x, y = q.popleft()
        for a, b in dxy:
            nx = x + a
            ny = y + b
            if 0<=nx<len(pic) and 0<=ny<len(pic) and not check[nx][ny]:
                if pic[nx][ny] in colorG:
                    check[nx][ny] = True
                    q.append((nx,ny))



def picture(pic, colorblind=False):
    cnt =0
    check = [[False] * n for _ in range(n)]
    for i in range(len(pic)):
        for j in range(len(pic[0])):
            if not check[i][j]:
                color =pic[i][j]
                if colorblind:
                    if color in ['R','G']:
                        colorG = ['R','G']
                    else:
                        colorG = ['B']
                else:
                    colorG = [color]
                bfs(check,pic,colorG,i,j)
                cnt+=1
    return cnt




print(picture(pic), picture(pic,colorblind=True))