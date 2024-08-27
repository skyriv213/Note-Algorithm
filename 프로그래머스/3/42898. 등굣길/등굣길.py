'''
M * N 크기의 지도
집(1,1) <-> 학교(m,n) 
물에 잠긴 지역 Puddles 따로 주어짐
오른쪽, 아래로만 움직여서 -> 방향은 이거
최단 경로를 1,000,000,007로 나눈 결과값 출력
'''
def solution(m, n, puddles):
    answer = 0
    puddles = [[q,p] for [p,q] in puddles]      
    maps = [[0 for i in range(m+1)] for _ in range(n+1)]
    maps[1][1] =1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j ==1: 
                continue
            if [i,j] in puddles:
                maps[i][j] = 0
            else:
                maps[i][j] = (maps[i-1][j] + maps[i][j-1])%1000000007
    return maps[n][m]