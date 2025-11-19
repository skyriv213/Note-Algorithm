from collections import deque

t = int(input())
for _ in range(t):
    p = list(input().replace("RR",""))

    n = int(input())

    if n == 0:
        trash = input()
        num = deque()
    else:
        num = deque(list(map(int,input()[1:-1].split(","))))
    reverse = False
    isError = False

    # print(*num)
    for s in p:
        if s=="R":
            reverse = not reverse
        else:
            if len(num)==0:
                isError = True
                break
            else:
                if reverse:
                    num.pop()
                else:
                    num.popleft()
    if isError:
        print("error")
    else:
        if reverse:
            num.reverse()
        print("["+','.join(map(str, num))+"]")

