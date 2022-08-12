n, m = map(int, input().split())
rice = list(map(int, input().split()))

start = 0
end = max(rice)

res = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in rice:
        if i > mid:
            total += (i - mid)
    if total >= m:
        # 떡을 넘치게 주면 안되니까 그때의 기록을 res에 기록
        res = mid
        start = mid + 1
    else :
        end = mid - 1

print(res)

