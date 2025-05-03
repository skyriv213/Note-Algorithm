'''
6 12 10
6층 , 방 12개, 10번째 손님
n/h = > 방 번호
n%w -> 층수
만약 n%h == 0 -> h -> 주어진 층수, roomNum은 그대로 방의 번호가 됨
'''

n = int(input())
for _ in range(n):
    h, w, n = map(int, input().split())  # 층수, 방 수, 손님
    floor = n % h # 층 수
    roomNum = n // h  +1 # 방 번호
    if floor==0 :
        floor = h
        roomNum -=1
    print(floor *100 + roomNum)
