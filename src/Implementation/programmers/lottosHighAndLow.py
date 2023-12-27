def solution(lottos, win_nums):
    answer = []
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}  # 맞은 숫자의 갯수 : 등수
    cnt = 0
    cnt0 = 0
    # 맞는 숫자의 갯수를 파악, 0으로 적힌 숫자도 파악
    for i in lottos:
        if i in win_nums:
            cnt += 1
        if i == 0:
            cnt0 += 1

    # 0으로 적힌 숫자와 맞는 숫자의 합은 최대 당첨순위의 경우, 맞는 숫자의 합으로는 최저 당첨순위의 합
    hope = cnt + cnt0

    return dic[hope], dic[cnt]