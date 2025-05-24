'''
note2에 적혀있는 m개의 숫자 순서대로 note1에 있으면 1, 없으면 0
'''

T = int(input())
for _ in range(T):
    n1 = int(input())
    note1 = sorted(list(map(int, input().split())))
    n2 = int(input())
    note2 = list(map(int,input().split()))
    res = []
    for i in note2:
        check = False
        left, right = 0, n1 - 1
        while left <= right:
            mid = (left+right)//2
            if note1[mid] == i:
                check = True
                break
            elif note1[mid] > i:
                right = mid - 1
            else:
                left = mid+1
        print(1 if check else 0)
