'''
종료 조건 : 주어진 row가 0이 되면 종료
            재귀를 반복할 때마다 row - 1 호출
주어진 조건 : left, right
            각 l,r을 기준으로 재귀함수는 반복 실행되어야 함
풀이
주어진 l,r을 기준으로 중간이 되는 구간에 x를 체크 해야 한다

답
-------------x-------------
-------x------------x------
----x--------x--------x----
'''

def tree(row, left, right):
    global s
    if row == 0:
        return
    m = (left+right)//2

    s[row-1][m-1] = 'X'
    tree(row - 1, left, m)
    tree(row - 1, m, right)

# row, left, right = map(int, input().split())
row, left, right= 6,0,70
s = [['-' for l in range(right)] for _ in range(row)]
tree(row, left, right)

for i in range(row-1, 0, -1):
    for j in range(right):
        print(s[i][j], end="")
    print()

