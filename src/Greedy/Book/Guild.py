n = int(input())
people = list(map(int, input().split()))
people.sort()

res, cnt = 0, 0  # 결과 및 그룹 당 인원

for i in people:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0

print(res)
