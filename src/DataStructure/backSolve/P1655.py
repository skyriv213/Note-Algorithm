import heapq
import sys

input = sys.stdin.readline

n = int(input())

left_num = []
right_num = []

for i in range(n):
    num = int(input())

    if len(left_num) == len(right_num):
        heapq.heappush(left_num, -num)

    else:
        heapq.heappush(right_num, num)

    if right_num and right_num[0]< -left_num[0]:
        left = heapq.heappop(left_num)
        right = heapq.heappop(right_num)

        heapq.heappush(left_num, -right)
        heapq.heappush(right_num, -left)

    print(-left_num[0])

