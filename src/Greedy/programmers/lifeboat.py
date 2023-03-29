'''
1. 배열 정렬
2. 투포인터 방식 선택
3. 가벼운 사람  + 무거운 사람을 했을 경우 limit가 채워지는 방향
'''


def solution(people, limit):
    answer = 0
    people = sorted(people)
    l, r = 0, len(people)-1

    while l <= r:
        if people[l] + people[r] > limit:
            answer += 1
            r -= 1
        else:
            answer += 1
            l += 1
            r -= 1

    return answer




