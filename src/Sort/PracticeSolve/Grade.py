n = int(input())

student = []

for _ in range(n):
    a, b = map(str, input().split())
    student.append((a, int(b)))

student = sorted(student, key = lambda x: x[1])

print(student)
