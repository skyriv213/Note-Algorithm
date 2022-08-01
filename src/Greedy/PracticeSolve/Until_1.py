n, k = map(int, input().split())
cnt = 0

while True:
    if n % k == 0:
        cnt += 1
        n = n // k
    else:
        cnt += 1
        n -= 1
    if n == 1:
        break
print(cnt)
