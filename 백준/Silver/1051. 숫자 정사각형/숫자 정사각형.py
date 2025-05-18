'''
정사각형이므로 같은 꼭지점이 동일한 숫자이면 됨
고로 한 점을 기준으로 거리만 체크하면 됨
'''
n,m = map(int, input().split())
rects = [list(input().strip()) for _ in range(n)]
res = 1
for i in range(n):
    for j in range(m):
        temp = min(n-i, m-j)
        for k in range(temp):
            if rects[i][j] == rects[i + k][j] and rects[i][j] == rects[i][j + k] and rects[i][j] == rects[i + k][j + k]:
                res = max(res, k+1)


print(res*res)


