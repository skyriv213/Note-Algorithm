input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    # 이 부분을 채워보세요!
    for i in range(len(array)):
        min_idx = i
        for j in range(len(array)):
            if array[j] > array[min_idx]:
                min_idx = j
                array[min_idx], array[i] = array[i], array[min_idx]


    return


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
