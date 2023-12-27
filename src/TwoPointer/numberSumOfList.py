'''
인덱스의 값을 비교하는 방식으로 접근
필요 변수 : start, end, sum, temp
start, end, sum = 0,0, 0

while 반복문 종료조건 : end가 리스트의 크기를 넘어섰을 때 종료
sum =< k:
    같을 경우
        해당 start와 end의 값을 temp 추가
    해당 end +=1을 하여 sum에 [end]값 추가

sum > k:
    sum -= sq[start]
    start +=1 start의 값 조절


배열 정리
sort key lambda 사용으로 정렬
마지막의 경우 크기를 의미하므로 0,1번째 원소만 가져와서 반환
'''


def solution(sequence, k):
    answer = []
    start, end, tot = 0, 0, sequence[0]
    temp = []
    sequence += [k + 1]
    while end < len(sequence) - 1:
        if tot <= k:
            if tot == k:
                temp.append((start, end, end - start))
            end += 1
            tot += sequence[end]
        else:
            start += 1
            tot -= sequence[start - 1]

    temp.sort(key=lambda tot: tot[2])

    return temp[0][0], temp[0][1]