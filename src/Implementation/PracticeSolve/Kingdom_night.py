'''
왕실의 나이트
8 x 8 좌표평면 입력받은 칸에 나이트 존재
나이트의 위치가 주어졌을 떄 나이트가 이동할 수 있는 경우의 수를 출력

문자열로 표현되는 열의 경우 아스키 코드 변환을 통해 숫자로 변환 후 계산한다.
'''
direction = [(-2, 1), (-2, -1),
             (2, 1), (2, -1),
             (1, 2), (1, -2),
             (-1, 2), (-1, -2)]

s = input()
row = int(s[1])
col = int(ord(s[0])) - int(ord('a')) + 1

res = 0
for i in direction:
    nr = row + i[0]
    nc = col + i[1]
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        res += 1

print(res)