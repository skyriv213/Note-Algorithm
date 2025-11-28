
t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    odd, even = 0, 0
    for i in num:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd == even or max(odd, even) % 2 == 0:
        print("heeda0528")
    else:

        print("amsminn")
