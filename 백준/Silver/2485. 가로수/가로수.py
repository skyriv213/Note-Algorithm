from math import gcd

def comGcd(minus):
    g = minus[0]
    for i in minus[1:]:
        g = gcd(g, i)
    return g

n = int(input())
tree = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
    exit()

minus = [tree[i]-tree[i-1] for i in range(1,len(tree))]

g = comGcd(minus)

total = (tree[-1] - tree[0]) // g + 1
print(total - n)
