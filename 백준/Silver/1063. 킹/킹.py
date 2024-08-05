import sys
from collections import deque

input = sys.stdin.readline

alpha = ["n", "A", "B", "C", "D", "E", "F", "G", "H"]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8]

directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1)
}

k, s, n = input().split()

king = [alpha.index(k[0]), int(k[1])]
stone = [alpha.index(s[0]), int(s[1])]
for i in range(int(n)):
    m = input().strip()
    move = directions[m]
    nk = [king[0] + move[0], king[1] + move[1]]
    if 1<= nk[0] <= 8 and 1<= nk[1] <= 8:
        if nk == stone:
            ns = [stone[0]+move[0], stone[1]+move[1]]
            if 1<= ns[0] <= 8 and 1<= ns[1] <= 8:
                king = nk
                stone = ns
        else:
            king = nk

print(alpha[king[0]] + str(king[1]))
print(alpha[stone[0]] + str(stone[1]))
