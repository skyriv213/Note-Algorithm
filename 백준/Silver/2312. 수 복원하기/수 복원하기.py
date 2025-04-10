import math

t = int(input())
for _ in range(t):
    n = int(input())
    num = []
    check = [False] * (int(math.sqrt(n)) + 2)

    # 에라토스테네스의 체로 sqrt(n)까지 소수 구하기
    for i in range(2, len(check)):
        if not check[i]:
            num.append(i)
            for j in range(i * i, len(check), i):
                check[j] = True

    for prime in num:
        if prime * prime > n:
            break
        count = 0
        while n % prime == 0:
            n //= prime
            count += 1
        if count > 0:
            print(prime, count)

        # 남은 n이 1보다 크면 그 자체가 소수임
    if n > 1:
        print(n, 1)



