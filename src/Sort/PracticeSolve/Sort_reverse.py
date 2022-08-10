n = int(input())
num = []
for _ in range(n):
    s = int(input())
    num.append(s)

num = sorted(num, reverse = True)

print(num)