def solution(mats, park):
    answer = -1
    n = len(park)
    m = len(park[0])
    board = [[0]*m for _ in range(n)]
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] =="-1":
                board[i][j] = 1
            else:
                board[i][j] =0
    
    dp = [[0]*m for _ in range(n)]
    max_size = 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if board[i][j] == 1:
                if i == 0 or j ==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1           
                max_size = max(max_size, dp[i][j])
    
    mats.sort(reverse = True)
    for i in mats:
        if i <= max_size:
            return i
    return answer