'''
n : 지방의 수
n개의 정수 : 각 지방의 요청
m : 최종 예산
출력 : 예산의 최댓값
'''

n = int(input())
area = sorted(list(map(int, input().split())))
m = int(input())
if sum(area)< m:
    print(area[-1])
else:
    left, right = 0,area[-1]
    res = 0
    while left <= right:
        mid = (left+right)//2
        total =0
        for i in area:
            if i <= mid:
                total+=i
            else:
                total += mid
        if total<=m:
            left =mid+1
            res = mid

        else:
            right = mid-1
    print(res)
