n = int(input())
work = list(map(int, input().split()))  # 체력 소모량
joy = list(map(int, input().split()))   # 얻는 기쁨

health = 100

# DP 테이블 초기화
dp = [[0 for _ in range(health + 1)] for _ in range(n + 1)]

# DP 테이블 작성
for i in range(1, n + 1):
    for w in range(1, health + 1):
        if work[i-1] < w:  # 현재 체력으로 만날 수 있는 경우, 한계치를 for문으로 배치
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-work[i-1]] + joy[i-1]) # 이전의 값과 비교하여 비교하기
        else:  # 만날 수 없는 경우
            dp[i][w] = dp[i-1][w]

# 최대 기쁨 찾기
max_joy = max(dp[n])

print(max_joy)
