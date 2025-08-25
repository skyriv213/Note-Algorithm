"""
두 도둑이 잡히지 않고 모든 물건을 훔칠 때, A도둑의 최소 흔적을 찾는 함수

:param info: 각 물건을 훔칠 때 A와 B가 남기는 흔적 정보 (2차원 배열)
:param n: A도둑이 잡히는 흔적의 최솟값
:param m: B도둑이 잡히는 흔적의 최솟값
:return: A도둑이 남긴 흔적의 최솟값 (불가능하면 -1)
"""
def solution(info, n, m):
    
    numItem= len(info)
    maxTrace = numItem*3 # 흔적의 개수는 1 이상 3 이하
    
    dp = [int(1e9)] *(maxTrace+1)
    
    dp[0] = 0
    
    for a,b in info:
        for j in range(maxTrace,-1,-1):
            if dp[j]==int(1e9):
                continue
            if j+a<=maxTrace:
                dp[j+a] = min(dp[j+a],dp[j])
            dp[j] = dp[j]+b
    answer =-1
    for j in range(maxTrace+1):
        if j< n and dp[j]<m:
            answer =j
            break
    return answer