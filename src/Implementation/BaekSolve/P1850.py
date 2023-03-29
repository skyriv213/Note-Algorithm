import math


# 이전에 알던 gcd
def gcd1(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a 
    else:
        return gcd1(b, a % b)


# 새롭게 알게된 gcd
def gcd2(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
print("1" * math.gcd(a, b))
