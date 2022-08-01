'''
1을 만드는 방법
주어진 n과 k를 이용해서 1을 만들어라
n은 주어진 수, k는 나눠지는 수
k로 나눠지지 않는 수는 1을 빼고 계산한다.
'''

n, k = map(int, input().split())
cnt = 0

while True:
    if n % k == 0:
        cnt += 1
        n = n // k
    else:
        cnt += 1
        n -= 1
    if n == 1:
        break
print(cnt)
