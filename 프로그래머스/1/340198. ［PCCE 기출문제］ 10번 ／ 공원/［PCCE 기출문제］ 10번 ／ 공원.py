def solution(mats, park):
    answer = 0
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "-1":
                park[i][j] = min(map(int, [park[i-1][j],park[i][j-1],park[i-1][j-1]]))+1
    print(park)
    return answer