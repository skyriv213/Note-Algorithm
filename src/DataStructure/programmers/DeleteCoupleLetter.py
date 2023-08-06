
def solution(s):
    answer = -1
    s1 = []
    for i in s:
        s1.append(i)
        if len(s1) > 1 and s1[-1] == s1[-2]:
            s1.pop()
            s1.pop()
    if len(s1) == 0 :
        return 1
    else:
        return 0
