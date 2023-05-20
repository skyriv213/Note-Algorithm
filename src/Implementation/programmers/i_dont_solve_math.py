def check_answer(answers, i, p, right, n):
    if answers[i] == p[(i % len(p))]:
        right[n] += 1


def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    right = [0, 0, 0]

    for i in range(len(answers)):
        check_answer(answers, i, p1, right,0)
        check_answer(answers, i, p2, right,1)
        check_answer(answers, i, p3, right,2)

    for idx, score in enumerate(right):
        if score == max(right):
            answer.append(idx + 1)

    return answer