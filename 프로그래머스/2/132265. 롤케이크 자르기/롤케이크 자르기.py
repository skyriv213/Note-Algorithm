'''
토핑의 갯수가 아닌 종류의 가짓수를 판별
종류의 체크를 위해 set 사용하여 중복 객체 삭제
그리고 반환값은 두개의 set의 크기가 동일하면 answer +=1
'''

def solution(topping):
    answer = 0
    sL = set()
    sR = set(topping)
    cR = {}
    for t in topping:
        cR[t] = cR.get(t,0)+1
    for t in topping:
        sL.add(t)
        cR[t]-=1
        if cR[t]==0:
            sR.remove(t)
        if len(sL) == len(sR):
            answer+=1

    # 시간초과 발생
    # for i in range(len(topping)):
    #     if len(set(topping[:i])) == len(set(topping[i:])):
    #         answer +=1
    

    
    
    return answer