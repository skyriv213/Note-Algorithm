'''
주어진 수의 합 중에서 가장 큰 값을 구해라
'''

n, m, k = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse = True)
res = (m // k) * k * num[0] + (m % k) * num[1]
print(res)


