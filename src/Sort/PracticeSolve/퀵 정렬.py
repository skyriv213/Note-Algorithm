'''
퀵 정렬
정렬 알고리즘 중 가장 많이 사용
'''
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(s, e):
    if s >= exit():  # 원소가 1개인 경우
        return
    pivot = s
    left = s + 1
    right = e
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= e and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > s and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈린다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(s, right - 1)
    quick_sort(right + 1, e)


# 파이썬 장점을 살린 퀵 정렬 소스코드
def quick_sort_python(array):
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫번째 원소
    tail = array[1:]  # 피벗 제외 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할 왼쪽
    right_side = [x for x in tail if x > pivot]  # 분할 오른쪽

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트 반환
    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)
