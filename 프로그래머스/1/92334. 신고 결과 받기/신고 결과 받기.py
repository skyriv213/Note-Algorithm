def solution(id_list, report, k):
    answer = []
    dic ={} # 신고 당한
    dic2 = {} # 신고한
    for i in id_list:
        dic[i] = set()
        dic2[i] =set()
    for i in report:
        a,b = i.split()
        dic[b].add(a) # 신고 당한
        dic2[a].add(b) # 신고한
    for i in id_list:
        temp = list(dic2[i])
        cnt = 0
        for j in temp:
            if len(dic[j]) >=k:
                cnt+=1
        answer.append(cnt)
    return answer