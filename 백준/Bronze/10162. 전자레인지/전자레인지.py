n =int(input())
res = []
for i in [300, 60,10]:
    res.append(n//i)
    n %=i
if n >0:
    print(-1)
else:
    print(' '.join(map(str, res)))
