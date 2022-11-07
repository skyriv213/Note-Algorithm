input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    if number in array:
        return True
    else:
        return False

    # 반복문 사용
    # for e in array:
    #     if numbers == e:
    #         return True
    #     else:
    #         retur False

result = is_number_exist(3, input)
print(result)