array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 87, 5, 9, 0, 3, 1, 6, 2, 4, 8]

count = [0] * 100001

# 배열의 원소를 인덱스로 갖는 count배열에 값을 1 추가
for i in array:
    count[i] += 1

# 카운트 배열에 값이 기록된 순간 값이 정렬
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = " ")