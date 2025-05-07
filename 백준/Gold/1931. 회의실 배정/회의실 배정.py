'''

'''

n = int(input())
room = []

for i in range(n):
    s, e = map(int, input().split())
    room.append([s, e])

room = sorted(room, key = lambda x: (x[1],x[0]))

cnt = 0
tmp = 0

for i, j in room:
    if i >= tmp:
        cnt += 1
        tmp = j

print(cnt)
