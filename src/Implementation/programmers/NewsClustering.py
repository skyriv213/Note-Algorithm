import math


def create_multiset(s):
    multiset = []
    for i in range(len(s) - 1):
        tmp = s[i:i + 2]
        if tmp.isalpha():
            multiset.append(tmp)
    return multiset


def solution(str1, str2):
    set1, set2 = create_multiset(str1.upper()), create_multiset(str2.upper())

    # 교집합 계산
    inter = []
    for i in set1:
        if i in set2:
            inter.append(i)
            set2.remove(i)

    # 합집합 계산
    union = len(set1) + len(set2)

    # 자카드 유사도 계산
    if union == 0:
        return 65536
    else:
        answer = len(inter) / union
        return int(answer * 65536)