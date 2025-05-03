'''
철수가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고
영희가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a

영희가 가진 카드들에 적힌 모든 숫자를 나눌 수 있고
철수가 가진 카드들에 적힌 모든 숫자들 중 하나도 나눌 수 없는 양의 정수 a

카드에 있는 정수가 아님
적힌 숫자를 모두 나눌수 있어야 하므로 범위는 각 배열의 가장 작은 원소까지

---------- 시간 초과 ----------
div 함수 선언
a에서 나눠지는 수 찾기 -> 해당 수를 temp 리스트에 삽입
b, temp를 순회, b의 원소가 temp로 나눠지는지 확인
-> 나눠지면 answer.append()
def div(arrayA,arrayB):
        
        n,minV = 1,min(arrayA)
        temp =deque([])
        
        while n <= minV:
            check = True # 이전 수에서도 나눠지는 지 판단
            
            for i in arrayA: # a 배열을 순회
                if i %n != 0: # 만약 나머지가 0이 아니라면 check를 false로 변경
                    check = False
                if not check :
                    break # check가 fasle라면 해당 반복문 중지
                    
            if check:
                temp.append(n)
            n+=1
            
        while temp:
            num = temp.popleft()
            check = True # 이전 수에서도 나눠지는 지 판단
            for i in arrayB:
                if i %num == 0: # 만약 나머지가 0이라면 check를 false로 변경
                    check = False
                if not check :
                    break # check가 fasle라면 해당 반복문 중지
            if check:
                answer.append(num)
        print(answer)
--------------------------------

-> 최대 공약수 접근
초반 접근 과정을 최대공약수로 처리 -> gcd 접근

'''
from math import gcd
from collections import deque
def solution(arrayA, arrayB):
    
    answer= [0]
    
    def make_gcd(num):
        curGcd = num[0]
        for i in num[1:]:
            curGcd = gcd(curGcd,i)
        return curGcd
    
    
    ga = make_gcd(arrayA)
    gb = make_gcd(arrayB)
    
    va = all(num%ga != 0 for num in arrayB)
    vb = all(num%gb != 0 for num in arrayA)
    
    if va:
        answer.append(ga)
    if vb:
        answer.append(gb)
    
    
    return max(answer)