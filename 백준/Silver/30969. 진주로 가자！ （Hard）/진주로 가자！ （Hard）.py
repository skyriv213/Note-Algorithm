import sys
input = sys.stdin.readline
n = int(input())
costTransportaion = [0 for _ in range(1001)]

cost = 0
ans =0

for _ in range(n):
    a,b = input().split()
    if int(b) > 1000:
        ans +=1
    else:
        if a =="jinju":
            cost = int(b)
        if cost != 0 and int(b)>cost:
            ans +=1
        if cost ==0:
            costTransportaion[int(b)]+=1

for i in range(cost+1, 1001):
    ans+=costTransportaion[i]


print(cost)
print(ans)
