def solution(s):
    answer = []
    te = ["{","}"]
    for i in te:
        s = s.replace(i,"")
    s =s.split(",")
    dic =dict()
    for i in s:
        i = int(i)
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    answer = sorted(dic, key=lambda x:dic[x],reverse=True)
    return answerN