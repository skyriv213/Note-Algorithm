input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    val = 0
    for i in array:
        if i <= 1 or val <= 1:
            val += i
        else:
            val *= i
    return val


result = find_max_plus_or_multiply(input)
print(result)
