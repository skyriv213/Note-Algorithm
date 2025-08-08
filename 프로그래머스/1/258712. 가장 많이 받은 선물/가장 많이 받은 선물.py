def solution(friends, gifts):
    answer = 0
    gift = [[0]*len(friends) for _ in range(len(friends))]
    for i in gifts:
        a,b = i.split()
        gift[friends.index(a)][friends.index(b)] += 1
    score = [[0]* 3 for _ in range(len(friends))]
    
    for i in range(len(score)):
        score[i][0] = sum(gift[i])
        score[i][1] = sum(gift[j][i] for j in range(len(friends)))
        score[i][2] = score[i][0] - score[i][1]
        # for j in range()
    nGift = [0] *len(friends)
    
    for i in range(len(gift)):
        for j in range(i+1, len(gift)):
            if gift[i][j] >gift[j][i]:
                nGift[i]+=1
            elif gift[i][j] <gift[j][i]:
                nGift[j]+=1
            else:
                if score[i][2] > score[j][2]:
                    nGift[i]+=1
                elif score[i][2] < score[j][2]:
                    nGift[j]+=1
    
    
    return max(nGift) if nGift else 0
