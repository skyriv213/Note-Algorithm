input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_val = 0
    for i in array:
        if i > max_val:
            max_val = i

    return max_val


result = find_max_num(input)
print(result)
