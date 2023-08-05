def solution(s):
    answer = []
    cnt, cnt0 = 0, 0
    while True:
        if s == '1':
            break
        cnt0 = cnt0 + s.count("0")
        s = s.replace("0", "")

        s = bin(len(s))[2:]

        cnt = cnt + 1

    answer = [cnt, cnt0]

    return answer