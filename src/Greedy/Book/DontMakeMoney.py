n = int(input())
money = sorted(list(map(int, input().split())))
# 만들수 없는 최소한의 정수를 찾기위해 target을 1로 지정, 만약 i의 경우가 기존의 수를 급격하게 넘어버리는 경우
# 반복문 종료 및
target = 1
for i in money:
    if target < i:
        break
    target += i

print(target)

