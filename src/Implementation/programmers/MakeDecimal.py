from itertools import combinations


def solution(nums):
    answer = 0
    a = sorted([sum(i) for i in combinations(nums, 3)])
    n = max(a) + 1
    m = int(n ** 0.5)
    sie = [True] * n

    for i in range(2, m + 1):
        if sie[i] == True:
            for j in range(2 * i, n, i):
                sie[j] = False

    for i in a:
        if sie[i] == True:
            answer += 1

    return answer