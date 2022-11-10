numbers = [1, 1, 1, 1, 1]
target_number = 3
res = 0


def plus_minus(number, target, idx, target_sum):
    if idx == len(number):
        if target_sum == target:
            global res
            res += 1
        return
    plus_minus(
        number, target, idx + 1, target_sum + number[idx]
    )
    plus_minus(
        number, target, idx + 1, target_sum - number[idx]
    )


plus_minus(numbers, target_number, 0, 0)  # 5를 반환해야 합니다!
print(res)
