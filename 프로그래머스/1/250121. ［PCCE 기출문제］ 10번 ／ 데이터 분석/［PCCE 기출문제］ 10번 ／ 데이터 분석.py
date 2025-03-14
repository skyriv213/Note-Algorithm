def solution(data, ext, val_ext, sort_by):
    answer = []
    for i in data:
        if ext == "code":
            if val_ext -i[0] >0:
                answer.append(i)
        elif ext == "date":
            if val_ext -i[1] >0:
                answer.append(i)
        elif ext == "maximum":
            if val_ext -i[2] >0:
                answer.append(i)
        else:
            if val_ext -i[3] >0:
                answer.append(i)
    if sort_by == "code":
        answer.sort(key = lambda x:x[0])
    elif sort_by == "date":
        answer.sort(key = lambda x:x[1])
    elif sort_by == "maximum":
        answer.sort(key = lambda x:x[2])
    else:
        answer.sort(key = lambda x:x[3])
    return answer