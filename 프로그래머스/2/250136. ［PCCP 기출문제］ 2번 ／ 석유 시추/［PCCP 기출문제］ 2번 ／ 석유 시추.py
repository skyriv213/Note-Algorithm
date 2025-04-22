from collections import deque

def solution(land):
    # 시간초과
#     def bfs(x,y,temp): 
#         dx,dy = [1,-1,0,0],[0,0,1,-1]
#         q = deque([(x,y)])
#         check =0
#         while q:
#             x,y = q.popleft()
#             if temp[x][y] == 0: 
#                 continue
#             check+=temp[x][y]
#             temp[x][y] = 0
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < len(temp) and 0 <= ny < len(temp[0]):
#                     if temp[nx][ny] == 1:
#                         q.append((nx, ny))
#         return check
                    
#     def check(num):
#         cnt = 0
#         temp = [row[:] for row in land]
#         for i in range(len(land)):
#             if temp[i][num] ==1:
#                 cnt += bfs(i,num,temp)
#         return cnt
            
#     answer = []
#     for i in range(len(land[0])):
    #         answer.append(check(i))
    row = len(land)
    col = len(land[0])
    check = [[False]* col for _ in range(row)]
    oil ={} # 열 : 석유량

    for i in range(row):
        for j in range(col):
            if land[i][j] == 1 and not check[i][j]:
                q = deque([(i,j)])
                check[i][j] = True
                oilS = 0
                affectCol =set()
                
                while q:
                    x,y = q.popleft()
                    oilS +=1
                    affectCol.add(y)

                    for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                        nx, ny = x+ dx, y+dy
                        if 0<=nx<row and 0<=ny<col:
                            if land[nx][ny] == 1 and not check[nx][ny]:
                                check[nx][ny]=True
                                q.append((nx,ny))
                for c in affectCol:
                    oil[c] = oil.get(c, 0)+oilS

    return max(oil.values()) if oil else 0