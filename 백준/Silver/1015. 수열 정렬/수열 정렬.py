n = int(input())
li = list(map(int, input().split()))
num = sorted(li)
res = []
for i in li:
    res.append(num.index(i))
    num[num.index(i)] = -1
print(*res)