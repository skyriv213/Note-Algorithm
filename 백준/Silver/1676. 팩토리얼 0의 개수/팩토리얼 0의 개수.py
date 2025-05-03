def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = str(factorial(int(input())))
cnt = 0
for i in range(len(n)-1,-1,-1):
    if n[i] != "0":
        break
    else:
        cnt+=1

print(cnt)