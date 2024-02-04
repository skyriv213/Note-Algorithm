def solution(s):
    answer = []
    dic = {}
    s1 = list(set(s))
    for i in s1:
        if i not in dic:
            dic[i] = -1
    for i in range(len(s)):
        if s[i] in dic and dic[s[i]] == -1:
            answer.append(dic[s[i]])
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i

    return answer