import sys

input = sys.stdin.readline
n = int(input())
# 숫자는 무조건 1이 포함
num = list(map(int, input().split()))
k = int(input())

num.sort()

# 다이나믹 프로그래밍으로 접근
# 메모제이션으로 접근
# dp.append(0) 해당 코드를 통해 미리 dp[i] 지정
# dp[0] = 0, dp[1] = 1, dp[i] = min(dp[i-1]+1, dp[i-num[2]]+num[2], dp[i-num[3]]+num[3] ----- -> for문으로 내부 반복]
# 이때 관건은 사용되는 숫자가 최소가 되는 경우의 수
# 출력문은 홀순 -> 짝수, 짝순 -> 홀수?
dp = [ 1e9 for _ in range(num[-1]*k +2)]
dp[0] = 0
for i in range(1, len(dp)):
    for j in num: # for를 통해 모든 원소 탐색 후 작은 값 +1을 통해 값을 계산
        if i >= j:
            dp[i] = min(dp[i], dp[i-j]+1)
    if dp[i] >k:
        s = "holsoon" if i %2 ==0 else "jjaksoon"
        print(f"{s} win at {i}")
        break