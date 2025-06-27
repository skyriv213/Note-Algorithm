def solution(board, moves):
    answer = []
    cnt = 0
    for k in moves:
        for i in range(len(board)):
            if board[i][k-1] !=0:
                answer.append(board[i][k-1])
                board[i][k-1] =0
                break
        while len(answer) >=2 and answer[-1] == answer[-2]:
            answer.pop()
            answer.pop()
            cnt+=2
            
    
    return cnt