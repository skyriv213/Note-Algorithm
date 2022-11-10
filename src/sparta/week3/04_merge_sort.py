array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    c = []
    # 이 부분을 채워보세요!
    a1, a2 = 0, 0
    while a1 < len(array1) and a2 < len(array2):
        if array1[a1] < array2[a2]:
            c.append(array1[a1])
            a1 += 1
        else:
            c.append(array2[a2])
            a2 += 1
    if a1 == len(array1):
        while a2< len(array2):
            c.append(array2[a2])
            a2 += 1


    if a2 == len(array2):
        while a1 < len(array1):
            c.append(array1[a1])
            a1 += 1


    return c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
