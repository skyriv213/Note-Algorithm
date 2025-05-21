S = int(input())
i =0
cnt =0
while True:
    cnt+=1
    i+=cnt
    if i > S:
        print(cnt-1)
        break
