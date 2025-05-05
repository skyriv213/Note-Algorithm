'''
안전 영역

2 <= N <= 100
1 <= N <= 100

2-3중 for문까진 ㄱㅊ을듯?

해당 숫자 초과되는 지역은 안전지역이라 판단 -> 이때 해당 안전지역의 갯수를 구하는 것이 목표

그리고 해당 안전지역의 갯수가 최대가 되는 물의 높이가 아닌 안전지역이 최대가 되었을 때 경우

입력값 : 지역 정보 -> 2차원 배열 사용
-> 처음 입력 후 max, min을 통해 최대 높이와 최소 높이 판단
answer = 0
판단:
for 문 최소 -> 최대로 진행
    check = area
    각 높이별 bfs 실행
    bfs(높이를 변수로 받음) -> dxy로 지역 이동, 해당 지역의 높이가 h 이하인 경우 false로 변환
        bfs 종료,
    종료 시 주변으로 안전구역 하나가 늘었다고 판단 cnt +=1
    if answer < cnt:
        answer = cnt

출력값 : 안전 지역의 최대 수 answer

'''
import sys
from collections import deque  # bfs를 위한 deque 선언

input = sys.stdin.readline
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
answer = 0
minV, maxV = int(1e9), 0
for i in area:
    for j in i:
        if j < minV:
            minV = j
        if j > maxV:
            maxV = j

if minV == maxV : # 모든 지역의 높이가 동일한 경우 해당 지역은 잠기거나 잠기지 않거나
    print(1)
    exit()

def bfs(h, check, a, b):  # 높이, 시작 좌표값 입력
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(a, b)])
    check[a][b] = True
    while q: # 반복문의 종료는 해당 좌표에서 시작된 안전지역의 탐색 끝
        x, y = q.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not check[nx][ny] and area[nx][ny] > h: # 안전지역만 체크 높이 이상의 지역만 순회
                    check[nx][ny] = True
                    q.append((nx, ny))
    return 1

for h in range(minV, maxV + 1):
    cnt = 0
    check = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if area[i][j] > h and not check[i][j]:
                cnt += bfs(h, check, i, j)
    if answer < cnt:
        answer = cnt

print(answer)
