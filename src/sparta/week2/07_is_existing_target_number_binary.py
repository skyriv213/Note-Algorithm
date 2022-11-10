finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    numbers.sort()
    start = 0
    end = len(numbers) - 1
    mid = (start + end) // 2

    while start <= end:
        if target == numbers[mid]:
            return True
        elif target < numbers[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)