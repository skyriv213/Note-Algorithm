def solution(arr1, arr2):
    # 행렬의 크기는 n*x * x *m =  n*m

    n = len(arr1)
    m = len(arr2[0])

    answer = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer