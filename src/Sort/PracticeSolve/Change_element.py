n, k = map(int, input().split())
num1 = sorted(list(map(int, input().split())))
num2 = sorted(list(map(int, input().split())), reverse = True)

for i in range(k):
    if num1[i] < num2[i]:
        num1[i], num2[i] = num2[i], num1[i]
    else:
        break

print(sum(num1))
