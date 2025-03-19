s, p = map(int, input().split())
st = input()
che = list(map(int, input().split()))

check = {"A": che[0], "C": che[1], "G": che[2], "T": che[3]}

res = 0
# for i in range(0, s - p + 1):
#     chArr = st[i:i + p]
#     temp = check.copy()
#
#     for j in chArr:
#         if temp[j] <= 0:  # 조건 최적화
#             break
#         temp[j] -= 1
#     else:
#         if all(val == 0 for val in temp.values()):
#             res += 1
base = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(s-p+1):
    flag = True
    if i ==0:
        for j in range(p):
            base[st[j]]+=1
    else:
        base[st[i+p-1]]+=1
        base[st[i-1]]-=1
    for i in ('A', 'C', 'G', 'T'):
        if base[i] < check[i]:
            flag = False
            break
    if flag:
        res += 1
print(res)
