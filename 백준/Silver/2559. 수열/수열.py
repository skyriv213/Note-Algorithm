n, m = map(int, input().split())
num = list(map(int, input().split()))
ans = []
left, right = 0, m
temp = sum(num[left:right])
ans.append(temp)
while right <n:
    right += 1
    temp = temp - num[left] + num[right-1]
    left += 1
    ans.append(temp)

print(max(ans))
