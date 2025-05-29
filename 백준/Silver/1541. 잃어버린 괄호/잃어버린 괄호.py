s = input().split("-")
res = sum(map(int, s[0].split("+"))) if s[0] else 0

for i in s[1:]:
    res -= sum(map(int,i.split("+")))
print(res)