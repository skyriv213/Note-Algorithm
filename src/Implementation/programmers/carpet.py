def solution(brown, yellow):
    answer = []

    key = [i for i in range(1, yellow // 2 + 1) if yellow % i == 0]
    key.append(yellow)

    for i in range(len(key)):
        x, y = i, len(key) - i - 1
        if key[x] + key[y] == brown / 2 - 2 and key[x] * key[y] == yellow:
            answer.append(key[x] + 2)
            answer.append(key[y] + 2)
            break

    return sorted(answer, reverse = True)