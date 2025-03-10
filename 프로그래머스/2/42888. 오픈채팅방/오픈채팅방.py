def solution(record):
    answer = []
    dic = {}
    res = []
    for i in record:
        s = i.split()
        if s[0] == "Enter":
            dic[s[1]] = s[2]
            answer.append(s[1]+" 님이 들어왔습니다.")
        elif s[0] =="Leave":
            answer.append(s[1]+" 님이 나갔습니다.")
        else:
            dic[s[1]] = s[2]
    for i in answer:
        temp = i.split()
        res.append(dic[temp[0]]+temp[1]+" "+temp[2])
        
            
        
    return res