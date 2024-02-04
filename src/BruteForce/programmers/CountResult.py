answer = 0


def recur(numbers, target, idx, total):
    global answer
    if idx == len(numbers):
        if total == target:
            answer += 1
        return
    recur(numbers, target, idx + 1, total + numbers[idx])
    recur(numbers, target, idx + 1, total - numbers[idx])


def solution(numbers, target):
    global answer
    recur(numbers, target, 0, 0)

    return answer