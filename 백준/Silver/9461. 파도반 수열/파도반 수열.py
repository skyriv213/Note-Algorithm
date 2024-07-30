n = int(input())

test = []
for i in range(n):
    a = int(input())
    test.append(a)

lis = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
tmp = max(test)
if tmp >= 10:
    for i in range(10, tmp):
        lis.append(lis[i-2] + lis[i-3])

for i in test:
    print(lis[i-1])
