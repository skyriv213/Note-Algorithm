import math

'''
기사의 공격력은 number의 약수 → 약수의 갯수를 파악해야함
limit는 기사의 공격력을 제한하는 역할. 만약 기사의 약수의 갯수보다 
limit가 작다면 해당 기사는 강제로 limit에 맞는 공격력으로 무기를 가져야함

1. 먼저 나이트 배열 선언 1-n까지 
2. 나이트의 배열의 원소의 약수의 갯수를 가지는 attack 배열을 구한다
3. 반복문 실행
4. attack이 limit를 넘겼는지 확인
5. 만약 넘겼으면 ans += power 아니면 해당 약수를 더함
--------------------------------------------------------------
개선
1. 나이트 리스트는 굳이 필요 x
2. 1~i까지의 이중 반복문은 너무 많은 시간 소모
    그렇기에 제곱근을 활용하여 탐색범위 절반으로 줄이기
풀이
1. 제곱근 활용 탐색 범위 줄이고 attack 구하기
2. attack 구하고 위의 조건에 맞춰서 answer 구하기
'''


def solution(number, limit, power):
    answer = 0
    attack = []

    for i in range(1, number + 1):
        tmp = 0
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                tmp += 2
            if i / j == j:
                tmp -= 1

        attack.append(tmp)

    for i in attack:
        if i > limit:
            answer += power
        else:
            answer += i
    return answer