a = int(input())

li = [64,32,16,8,4,2,1]
cnt = 0

for i in range(len(li)):
    if a >=li[i]:
        cnt+=1
        a-=li[i]
    if a==0:
        break

print(cnt)