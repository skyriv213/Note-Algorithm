'''
테이블 튜플 정렬
- col번째 컬럼의 값을 기준으로 오름차순, 해당 값 동일시 첫번째 컬럼 내림차순
정렬된 데이터에서 S_i를 i번째 행의 튜플에 대해 각 컬럼의 값을 i로 나누고 나머지들의 합으로 정의
row begin-> end에서의 모든 s_i를 누적하여 bitwise XOR한 값으로 해시 값 반환


'''

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))
    hashS =[]
    for i in range(row_begin-1, row_end):
        sum = 0
        for j in range(len(data[i])):
            sum+=data[i][j]%(i+1)
        hashS.append(sum)
    answer = hashS[0]
    for i in range(1,len(hashS)):
        answer^=hashS[i]
    return answer