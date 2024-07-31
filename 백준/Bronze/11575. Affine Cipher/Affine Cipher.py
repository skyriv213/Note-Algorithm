n = int(input())
num = [i for i in range(0, 26)]
lst = [chr(x) for x in range(65, 91)]
for i in range(n):
    a, b = map(int, input().split())
    s = input()
    tm = []
    for j in s:
        tm.append(lst[(a * num[lst.index(j)] + b) % 26])
    print("".join(tm))

