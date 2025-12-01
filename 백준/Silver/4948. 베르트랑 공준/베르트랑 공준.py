import math

maxV = 123456 * 2 + 1

isPrime = [True] * maxV
isPrime[0] = isPrime[1] = False

for i in range(2, int(math.sqrt(maxV)) + 1):
    if isPrime[i]:
        for j in range(i * i, maxV, i):
            isPrime[j] = False

while True:
    num = int(input())
    if num == 0:
        break
    cnt = 0
    for i in range(num + 1, 2 * num + 1):
        if isPrime[i]:
            cnt += 1
    print(cnt)