'''
방향 이동 dx, dy, di로 체크
이동 거리 : 이동할 때마다 +=1
중복 거리 처리 : Set으로 처리 ({(출발 좌표),(도착 좌표)})
'''

def solution(dirs):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    di = ["R","U","L","D"]
    
    answer = 0
    pos = set()
    px,py = 0,0
    for i in dirs:
        if i in di:
            nx = px + dx[di.index(i)]
            ny = py + dy[di.index(i)]
            if -5 <= nx <= 5 and -5 <=ny<=5:
                if ((px,py),(nx,ny)) not in pos :
                    answer +=1
                    pos.add(((px,py),(nx,ny)))
                    pos.add(((nx,ny),(px,py)))
                px = nx
                py = ny    
    
    return answer