from collections import Counter

def solution(weights):
    answer = 0
    cnt = Counter(weights)
    for i in range(100,1001):
        if cnt[i]>0:
            answer += (cnt[i] * (cnt[i]-1))/2 # 1:1
            answer += cnt[i]*cnt[i*3/2] # 2:3
            answer += cnt[i]*cnt[i*2] # 2:4
            answer += cnt[i]*cnt[i*4/3] # 3:4
    return answer