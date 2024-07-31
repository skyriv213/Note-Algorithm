from collections import deque

s = input()

n = list(s)
tmp = []

n1 = deque(n)

while True:
    n1.rotate(1)
    tmp.append(int("".join(n1)))
    if s == ("".join(n1)):
        break

print(sum(tmp))
