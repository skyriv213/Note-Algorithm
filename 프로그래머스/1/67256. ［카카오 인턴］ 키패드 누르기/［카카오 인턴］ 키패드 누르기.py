

def solution(numbers, hand):
    answer = []
    key_pos = {
        1: (0,0), 2:(0,1), 3:(0,2),
        4: (1,0), 5:(1,1), 6:(1,2),
        7: (2,0), 8:(2,1), 9:(2,2),
        '*':(3,0),0:(3,1), '#':(3,2)
    }
    
    lh,rh = key_pos['*'], key_pos['#']
    
    for num in numbers:
        if num in [1,4,7,'*']:
            answer.append('L')
            lh = key_pos[num]
        elif num in [3,6,9,'#']:
            answer.append('R')
            rh = key_pos[num]
        else:
            target = key_pos[num]
            ld = abs(lh[0]-target[0]) + abs(lh[1]-target[1])
            rd = abs(rh[0]-target[0]) + abs(rh[1]-target[1])
            if ld < rd or (ld ==rd and hand == "left"):
                answer.append('L')
                lh = target
            else:
                answer.append('R')
                rh = target
            
    return ''.join(answer)