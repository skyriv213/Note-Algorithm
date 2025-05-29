t = int(input())
for _ in range(t):
    c = int(input())
    res = []
    for i in [25,10, 5,1]:
        res.append(c//i)
        c %=i
    print(' '.join(map(str,res)))
