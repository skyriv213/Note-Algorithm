import sys

input = sys.stdin.readline

n = int(input())
en = set()
for _ in range(n):
    n,m= input().split()
    if m == "enter":
        en.add(n)
    else:
        en.remove(n)

for name in sorted(en, reverse=True):
    print(name)
