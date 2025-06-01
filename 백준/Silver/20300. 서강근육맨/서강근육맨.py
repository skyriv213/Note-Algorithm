n = int(input())
mus = sorted(list(map(int, input().split())))
res = 0

if n %2 !=0:
    res = mus[-1]
    mus = mus[:-1]

for i in range(len(mus)//2):
    res = max(res, mus[i]+mus[-(i+1)])

print(res)
