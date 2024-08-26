'''
DP 사용
조건 파악
주어진 N을 이용하여 사칙연산을 통해 number 만들기
그리고 이때의 최소 사용횟수를 return

만약 최솟값이 8이상이면 return -1
'''
def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)]
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)
                    if op2!=0:
                        dp[i].add(op1//op2)
        if number in dp[i]:
            return i
    return -1