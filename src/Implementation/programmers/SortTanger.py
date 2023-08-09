'''
문제풀이를 진행할 때 주어진 k에서 바로 빼면서 진행하는 것이 아닌
하나의 s같은 값을 지정해서 그 값을 주어진 k와 비교하기
주어진 k로 바로 비교를 하면 값에 변화가 생김

문제풀이
dict 자료구조 사용
dict을 두번째 원소기준 내림차순으로 정렬
만약 내림차순으로 정렬 시 k를 넘은 값이 있으면 1을 return

반복문을 진행하면서
주어진 k값과 비교하려는 s를 비교하기 - k에 -를 하면서 직접적인 접근은 x
만약 주어진 값과 s의 비교시 넘어가거나 같다면 반복문 종료 후 answer를 return 
'''
def solution(k, tangerine):
    answer = 0
    s = 0
    dic = {}
    for i in tangerine:
        if not i in dic:
            dic[i]=1
        else:
            dic[i]+=1
    tanger = sorted(dic.items(),key = lambda x :x[1] ,reverse =True)
    if tanger[0][1] >= k:
        return 1
    for i,item in enumerate(tanger):
        if s < k:
            s+=item[1]
            answer+=1
        else:
            break
    return answer