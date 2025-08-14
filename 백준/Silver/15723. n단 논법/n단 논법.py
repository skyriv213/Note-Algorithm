'''
첫째 줄에 정수 n(2 ≤ n ≤ 26)이 주어진다.

둘째 줄부터 n개의 줄에 걸쳐 각 줄에 전제가 하나씩 주어진다. 전제는 모두 a is b의 형식으로 주어지며 a와 b는 서로 다른 임의의 알파벳 소문자이다. 특별한 명시는 없지만 모든 전제는 “모든 a는 b이다”라는 의미이다. 하지만 “모든 b는 a이다”의 의미는 될 수 없다. 또한 a는 b이면서 c일 수 없으나, a와 b가 동시에 c일 수는 있다.

n + 2번째 줄에 정수 m(1 ≤ m ≤ 10)이 주어진다. 그 다음 m개의 줄에 걸쳐 각 줄에 하나의 결론이 전제와 같은 형식으로 주어진다.

플로이드-워셜로 접근
'''


def translating(temp):
    return ord(temp[0])-ord('a'),ord(temp[-1])-ord('a')

n = int(input())
graph = [[0 for _ in range(26)] for i in range(26)]

for _ in range(n):
    temp = input().split()
    a,b = translating(temp)
    graph[a][b] = 1


for k in range(26):
    for i in range(26):
        for j in range(26):
            if graph[i][k] and graph[k][j]:
                graph[i][j]  =1

n = int(input())

for _ in range(n):
    temp = input().split()
    a,b = translating(temp)

    print("T") if graph[a][b] else print("F")



