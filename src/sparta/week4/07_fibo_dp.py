input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

#
# def fibo_dynamic_programming(n, fibo_memo):
#     # 구현해보세요!
#     memo=[0,1,1]
#     for i in range(3,n+1):
#         memo.append((memo[i-1]+memo[i-2]))
#     return memo[n]

# 딕셔너리 및 재귀 이용
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


print(fibo_dynamic_programming(input, memo))