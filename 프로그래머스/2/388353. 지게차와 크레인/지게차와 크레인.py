def fork(storage, box):
    index =[] 
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] == box:
                for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nx,ny = i+dx , j+ dy
                    if storage[nx][ny] == "0":
                        index.append((i,j))
                        break
    for i, j in index:
        storage[i][j] = "0"
        isOutside(storage, i,j)
        
def crane(storage, box):
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] == box:
                storage[i][j] = "1"
                isOutside(storage, i, j)
                
def isOutside(storage, x,y):
    outSide = False
    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx, ny = x+dx, y+dy
        if storage[nx][ny] == "0":
            storage[x][y] = "0"
            outSide = True
            break
    if outSide:
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x+dx, y+dy
            if storage[nx][ny]=="1":
                storage[x][y] = "0"
                isOutside(storage, nx, ny)


def solution(storage, requests):
    answer = 0
    
    storage = [list("0"+i+"0") for i in storage]
    storage.insert(0,list("0" *len(storage[0])))
    storage.append(list("0" *len(storage[0])))
    
    for q in requests:
        if len(q) == 1:
            fork(storage, q)
        else:
            crane(storage, q[0])
            
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] not in ["0","1"]:
                answer+=1
                
    print(storage)
    return answer