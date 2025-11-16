n = int(input())

num = []
for i in range(n):
    num.append(input())

# 3
# 1212345
# 1212356
# 0033445
ans = 1
for i in range(1,len(num[0])+1):
    temp = []
    for j in range(n):
        temp.append(num[j][-i:])

    if n == len(set(temp)):
        break
    else:
        ans+=1

print(ans)