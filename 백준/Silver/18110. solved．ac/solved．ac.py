import sys

input =  sys.stdin.readline
n = int(input())
if n == 0:
    print(0)
else:
    diffi = [int(input()) for _ in range(n)]
    num = int((len(diffi) * 0.15)+0.5)
    diffi = sorted(diffi)
    # for i in range(num):
    #     diffi.pop(0)
    #     diffi.pop(-1)
    diffi = diffi[num:n - num]

    print(int((sum(diffi) / len(diffi))+0.5))