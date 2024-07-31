p,n = map(int, input().split())
acc = list(map(int, input().split()))

acc.sort()
cnt = 0
for i in acc:
    if p >= 200:
        break
    cnt +=1
    p+=i

print(cnt)