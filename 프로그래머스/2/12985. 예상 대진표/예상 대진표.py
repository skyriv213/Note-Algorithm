def solution(n,a,b):
    answer=0
    while a!=b:
        if a%2!=0:
            a+=1
        a//=2
        if b%2!=0:
            b+=1
        b//=2    
        # if a//2 == b//2:
        #     return answer
        answer=+1
    

    return answer