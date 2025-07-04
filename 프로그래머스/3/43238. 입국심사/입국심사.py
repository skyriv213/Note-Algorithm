'''
이분 탐색, 
n은 사람의 수
times는 심사관의 수
return은 시간의 최솟값

temp = 0부터 증가 -> times의 최솟값부터 증가, 어차피 입국심사를 기다리는 인원은 1명 이상 1e9 이하
이분 탐색으로 최소값과 최댓값의 지점을 잡아야함. 
그리고 temp를 진행시 temp의 값을 +1이 아닌 +a로 잡아야함 -> 1의 경우 너무 오래걸려서 시간초과 발생할 수 있음

이분 탐색이므로 시작값과 끝값을 지정해야할거같은데 어떻게 해야하지..?



temp // times 진행 해당 몫의 합이 n이 되는 경우가 최소 경우

'''

def solution(n, times):
    start, end = min(times), max(times)*n
    answer = end
    while start<=end:
        time = (start +end)//2
        total = sum(time//t for t in times)        
        if total < n :
            start = time+1
        else:
            end = time-1
            answer = time

    return answer