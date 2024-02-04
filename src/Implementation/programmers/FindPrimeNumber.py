import itertools


def solution(numbers):
    answer = 0
    num = [i for i in numbers]
    num1 = []
    for i in range(1, len(numbers) + 1):
        num1 += itertools.permutations(num, i)
    num1 = list(set(num1))
    num2 = []
    for i in num1:
        a = ''.join(i)
        if int(a) > 1 and a[0] != '0':
            num2.append(int(a))

    tf = [True] * (max(num2) + 1)

    for i in range(2, max(num2) + 1):
        if tf[i] == True:
            for j in range(i * 2, max(num2) + 1, i):
                tf[j] = False
    cnt = 0
    for i in num2:
        if tf[i] == True:
            cnt += 1
    return cnt
