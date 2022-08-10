'''
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
시간 복잡도는 O(n) = 데이터의 개수가 n개일때 최대
'''


def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며 진행
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하시오")
data = input().split()
n = int(data[0])  # 원소의 갯수
target = data[1]  # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하시오. 띄어쓰기 구분은 한 칸")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
