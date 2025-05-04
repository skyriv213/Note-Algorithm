t = int(input())

people = [list(input()) for _ in range(t)]
INF = int(1e9)
check = [[INF]*t for _ in range(t)]

for i in range(t):
    for j in range(t):
        if i == j:
            check[i][j] = 0  # 자기 자신은 0
        elif people[i][j] == 'Y':
            check[i][j] = 1  # 직접 친구는 거리 1

for k in range(t):
    for i in range(t):
        for j in range(t):
            check[i][j] = min(check[i][j], check[i][k]+check[k][j])
            
maxF = 0
for i in check:
    temp =0
    for j in i:
        if 0<j <=2 :
            temp+=1
    maxF = max(maxF,temp)

print(maxF)
