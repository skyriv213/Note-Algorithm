'''
전형적인 타일링 문제이다 해당 문제의 규칙을 찾아 점화식을 구하고
그 점화식을 그대로 구현해주면 된다.
'''

n = int(input())

d = [0] * 1001
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) & 796796

print(d[n])