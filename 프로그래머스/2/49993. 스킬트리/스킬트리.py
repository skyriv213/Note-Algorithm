import re

def solution(skill, skill_trees):
    answer = 0
    temp = []
    for i in skill_trees:
        temp.append(re.sub(f"[^{skill}]", '', i))
        
    for i in temp:
        if i == '':
            answer +=1
        else:
            if i in skill and i[0]==skill[0]:
                answer+=1
    return answer