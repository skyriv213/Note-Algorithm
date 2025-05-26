'''
이분 탐색
m 명의 조카, n 개의 과자
과자의 길이
나눠준 과자의 길이가 다르면 실패, 모든 조카에게 같은 길이 막대 과자 나눠줘야함
과자의 길이는 나눠질수있지만 합치기는 안됨, -> mid로 나누면서 몫이 m개 이상 res 갱신

'''

m, n = map(int, input().split())
cookie = list(map(int, input().split()))
left, right = 1, max(cookie)
res = 0
while left <= right:
    mid = (left +right) // 2
    temp = sum(c//mid for c in cookie)
    if temp >= m:
        left = mid + 1
        res = mid
    else:
        right = mid - 1

print(res)
