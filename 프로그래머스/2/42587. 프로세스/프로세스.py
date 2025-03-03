from collections import deque

def solution(priorities, location):
    cnt = 0
    p = deque([(index,x) for index,x in enumerate(priorities)])
    maxV = max(priorities)
    while p:
        index , x = p.popleft()
        if x == maxV and index == location:
            return cnt+1
        elif x == maxV: 
            priorities.remove(x)
            maxV = max(priorities)
            cnt+=1
        else:
            p.append((index,x))
            
    return -1