import math

input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    '''

    :param number:
    :return:
    에라토스테네스의 체 구현
    1. 이중 반복문
    2. 소수이므로 2부터 input까지 반복문 순회
    3. 각
    '''
    arr = [True] * (number + 1)
    arr[0] = False
    arr[1] = False
    for i in range(2, input):
        for j in range(1, int(math.sqrt(number)) + 1):
            if j == 1 or i * j > number:
                continue
            else:
                arr[i * j] = False

    arr2 = []
    for i in range(0, len(arr)):
        if arr[i]:
            arr2.append(i)
    return arr2


result = find_prime_list_under_number(input)
print(result)

