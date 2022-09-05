n = input()

res = 0
for i in range(0, len(n)):
    num = int(i)
    if num < 1:
        res += num
    else:
        res *= num
print(num)
