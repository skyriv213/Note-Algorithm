finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    start = 0
    end = len(array) - 1
    mid = (start + end) // 2

    while start <= end:
        if target == array[mid]:
            return True
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)


