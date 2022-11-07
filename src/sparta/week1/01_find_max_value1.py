input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for n in array:
        for compare_n in array:
            if n < compare_n:
                break
        else:
            return n


result = find_max_num(input)
print(result)
