'''
주어진 방향으로 이동할 때 공원을 벗어나는지 확인
if (0<=nx,ny < len(park))
주어진 방향으로 이동 중 장애물을 만나는지 확인
for(0~n):
if nx,ny != 장애물:
    진행
    
모든 명령 수행 후 강아지의 위치

'''

def solution(park, routes):
    H,W = len(park), len(park[0])
    
    moves = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    
    sx,sy = 0,0
    newPark = []
    for p in park:
        newPark.append(list(p))
        
    for i in range(H):
        for j in range(W):
            if newPark[i][j] == "S":
                sx,sy = j,i

    for r in routes:
        temp = r.split(" ")
        d = temp[0]
        cnt = int(temp[1])
        nx,ny = sx,sy
        dy,dx = moves[d]
        check = True

        for _ in range(cnt):
            nx += dx
            ny += dy
            if not (0<=nx<W and 0<=ny <H) or newPark[ny][nx]=='X' :
                check = False
                break

        if check:
            sx,sy = nx,ny
                
                
    return [sy,sx]