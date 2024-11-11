'''
want:number를 가진 set
discount 배열 순회 - for문
- 현재위치에서 10개
  리스트 컴프레션 - want:number 리스트 전부다 충족 = answer +=1
'''

def solution(want, number, discount):
    answer = 0
    obj = set()
    for i in range(len(want)):
        obj.add((want[i],number[i]))
    # print(obj)
    # sorted(obj)
    # print(obj)
    for i in range(len(discount)-9):
        temp_set = set()
        temp_list = discount[i:i+10]
        check_li = set(temp_list)
        for i in temp_list:
            if i in check_li:
                temp_set.add((i,temp_list.count(i)))
                check_li.remove(i)
        # print(temp_set)
        if sorted(temp_set) == sorted(obj):
            answer+=1
    return answer