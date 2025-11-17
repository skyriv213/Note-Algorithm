'''
탱커 전투력 A, 딜러 전투력 B  Ax + By 최대가 되야함
탱커 비용 PA, 딜러비용 PB
PA X + Pb Y <= n

재귀는 시간 초과 발생
for 문으로 변경

'''
# import sys
# 
# sys.setrecursionlimit(2000000)

n = int(input())
a, pa, b, pb = map(int, input().split())
ans = [0, 0]
#
attack = 0
#
# def score(x,y):
#     return a * x + b * y
#
#
# def bt(x):
#     global attack,ans
#     cx = pa*x
#     if cx>n:
#         return
#
#     remainBudget = n-cx
#     y = remainBudget//pb
#
#     temp = score(x,y)
#     if attack <temp:
#         attack = temp
#         ans[0] = x
#         ans[1] = y
#     if cx+pb*y<=n:
#         bt(x+1)
#
# bt(0)

for x in range((n // pa) + 1):
    rb = n - (pa * x)
    y = rb // pb
    score = a * x + b * y
    if score > attack:
        attack = score
        ans[0] = x
        ans[1] = y

print(ans[0], ans[1])
