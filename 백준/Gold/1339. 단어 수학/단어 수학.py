'''
가중치를 생각해야함
가중치 = 자릿수의 위치와 각 숫자가 배치되었을때 최댓값이 나오는 경우
-> 가장 큰 자릿수부터 9~1 순으로 숫자를 낮춰가면서 배치, 다만 이때 위치 값은 고려대상이고 등장 횟수 또한 추가해서 계산해야함
defaultdict를 사용 -> dictionary 사용
해당 글자가 등장할때마다 가중치를 합산

'''

from collections import defaultdict

n = int(input())
s = [input() for _ in range(n)]
alpa = defaultdict(int)
for i in s:
    l = len(i)
    for j, char in enumerate(i):
        alpa[char] += 10 ** (l - j - 1) # 자릿수로 가중치 덧셈, 할당

sortAlpa = sorted(alpa.items(), key=lambda x: -x[1])
# print(sortAlpa)

dic = {}
num = 9
for char, _ in sortAlpa:
    dic[char] = num
    num -= 1

res = 0
for i in s:
    temp = ''
    for j in i:
        temp += str(dic[j])
    res += int(temp)

print(res)
