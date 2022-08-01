'''
정수 n이 입력이 되면 00시 00분 00초 부터 n시 59분 59초까지 모든 시각 중 m이 하나라도 포함이 되는 경우의 수 구하기
'''

n, m = map(int, input().split())

m = str(m)

cnt = 0

for hour in range(0, n + 1):
    for min in range(0, 60):
        for sec in range(0, 60):
            if m in str(hour) + str(min) + str(sec):
                cnt += 1

print(cnt)
