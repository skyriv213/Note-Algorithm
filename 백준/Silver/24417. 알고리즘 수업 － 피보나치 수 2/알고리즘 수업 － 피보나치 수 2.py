n = int(input())

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = (a + b) % 1000000007, a % 1000000007
    return a


def fibnacci(n):
    # cnt = 0
    # for i in range(3, n + 1):
    #     cnt += 1
    # return cnt % 1000000007
    return n-2


print(fib(n), fibnacci(n))
