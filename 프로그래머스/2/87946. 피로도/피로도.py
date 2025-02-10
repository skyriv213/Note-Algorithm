def backtracking(c,k,ds):
    global answer

    for i,d in enumerate(ds):
        if k >= d[0]:
            new_ds = ds.copy()
            new_ds.pop(i)
            clear = backtracking(c+1, k-d[1],new_ds)
            if answer < clear:
                answer = clear
    return c

def solution(k, dungeons):
    global answer
    answer = -1
    
    backtracking(0,k,dungeons)
    return answer