def binary(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if check[mid] == target:
            return True
        elif check[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


n = int(input())
check = list(map(int, input().split()))
check.sort()

m = int(input())
parts = list(map(int, input().split()))

for i in parts:
    if binary(i):
        print("yes", end = " ")
    else:
        print("no", end = " ")
