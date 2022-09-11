# 풀이의 경우 n번 반복하는 반복문과 그안에 n-i만큼 반복문이 존재
# 브루트포스의 경우 시간복잡도는 o(n*(n-1)!) = o(n!)이라고 볼 수 있다.
#
# 해설지의 경우 그리디의 방법을 채택
# 한 번의 반복문으로 이뤄져있고 그에 따라 무게인 m번의 탐색 후 반복문 종료,
# 시간복잡도는 o(m) or o(n)이라고 볼 수 있다. 


n, m = map(int, input().split())
ball = sorted(list(map(int, input().split())))
cnt = 0
# 브루트 포스
num = []
for i in range(n):
    num.append((ball[i], i))

for i in range(n):
    for j in range(i, n):
        if num[i][0] == num[j][0]:
            continue
        else:
            cnt += 1

print(cnt)

# 해설지
# arr = [0] * 11
# for x in ball:
#     arr[x] += 1
#
# # 1부터 m까지 각 무게에 대하여 처리
# for i in range(1, m + 1):
#     n -= arr[i]
#     cnt += arr[i] * n
