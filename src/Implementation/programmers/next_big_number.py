'''
1. 주어진 수를 이진수로 변환
2. 주어진 수에서 1의 갯수를 count
3. n이후의 수를 반복하여 2진수로 변환
4. 변환을 반복하면서 기존의
'''


def solution(n):
    answer = num(n)
    while 1:
        n = n + 1
        impl = num(n)
        if impl == answer:
            break
    return n


def num(a):
    temp = 0
    s = str(bin(a)[2:])
    for i in s:
        if i == '1':
            temp += 1

    return temp
