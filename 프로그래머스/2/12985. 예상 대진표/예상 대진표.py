import math
def solution(n,a,b):
    answer = 1

    while a!=b :
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer+=1
        if a==b :
            answer-=1
        
    return answer
