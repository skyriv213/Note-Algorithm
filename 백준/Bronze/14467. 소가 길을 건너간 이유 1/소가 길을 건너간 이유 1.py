n = int(input())

'''
소가 움직였는지 판단
소의 위치가 변경이 되었는지 파악
'''

cow = [[] for i in range(11)]
for i in range(n):
    c, p = map(int, input().split())
    cow[c].append(p)
cnt = 0
for i in cow:
    if len(i) != 0:
        tmp = i[0]
        for j in i:
            if tmp != j:
                cnt += 1
                tmp = j

print(cnt)