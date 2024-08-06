from collections import deque

n, k = map(int, input().split())
people = deque([i for i in range(1, n + 1)])

res = []

while people:
    people.rotate(-(k-1))  # k-1번 왼쪽으로 회전
    res.append(people.popleft())  # k번째 사람을 제거하고 결과에 추가

print("<", ", ".join(map(str, res)), ">", sep="")
