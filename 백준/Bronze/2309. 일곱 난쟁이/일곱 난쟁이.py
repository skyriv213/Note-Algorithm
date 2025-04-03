from itertools import *

li = []
for _ in range(9):
    li.append(int(input()))

s = combinations(li, 7)
for i in s:
    li2 = list(i)
    if sum(li2) == 100:
        li2.sort()
        for i in li2:
            print(i)
        break



