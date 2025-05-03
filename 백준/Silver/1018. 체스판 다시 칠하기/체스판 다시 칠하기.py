'''
mn 단위 정사각형, m*n의 크기의 보드

N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
-> 해당 구문에서 최대 조회의 경우는 n,m이 50,50인 경우

mn 단위 정사각형, m*n의 크기의 보드

N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다.
-> 해당 구문에서 최대 조회의 경우는 n,m이 50,50인 경우

'''
n,m = map(int, input().split())

chess = [list(input().strip()) for _ in range(n)]

answer = []

for i in range(n-7):
    for j in range(m-7):
        wI = 0
        bI = 0

        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 ==0:
                    if chess[a][b] != "W":
                        wI+=1
                    else:
                        bI += 1
                else:
                    if chess[a][b] != "W":
                        bI+=1
                    else:
                        wI+=1
    
        answer.append(wI)
        answer.append(bI)

print(min(answer))
