def solution(keymap, targets):
    answer = []
    idx = {}

    for i in range(ord('A'),ord('Z')+1):
        idx[chr(i)] = 1e9
    for k in keymap:
        for i in range(len(k)):
            idx[k[i]] = min(idx[k[i]],i+1)      
    for i in targets:
        sum = 0
        for j in i:
            # if not idx[j] == 1e9:
            sum+=idx[j]
                
        if sum >= 1e9: 
            answer.append(-1)
        else:
            answer.append(sum)
    return answer