'''
사범은 0,0
학생들은 좌표평면으로 (x,y)로 존재

-> 틀림
for x,y in sorted(stu,key= lambda x: abs(0-x[0])):
    for i in range(2,maxv):
        if (x*i,y*i) in stu:
            stu.remove((x*i,y*i))

후에 직접적으로 배수가 되는 항목을 찾아 제거하면 오류 발생

넣는 순간에 판단해야함

'''
import sys
# input = sys.stdin.readline
from math import gcd

n = int(input())
stu = set()
for _ in range(n):
    x,y = map(int, input().split())
    g = gcd(x,y)
    stu.add((x/g,y/g))

print(len(stu))