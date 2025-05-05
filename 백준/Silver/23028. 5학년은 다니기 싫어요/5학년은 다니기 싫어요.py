import sys
input = sys.stdin.readline

N, A, B = map(int, input().strip().split())

major = []      # 전공 학점
non_major = []  # 비전공 학점(학기마다 정해진 과목의 수)
for _ in range(10):
    X, Y = map(int, input().strip().split())    # 전공 과목 개수와 비전공 과목 개수
    major.append(X)
    non_major.append(Y)

semester = 8 - N    # 남은 학기
if B >= 130 and A >= 66:
    print("Nice")
else:
    # 전체 학점을 채워야 되는데 우선순위 1순위 : 전공 학점
    for i in range(semester):
        A += major[i] * 3
        B += major[i] * 3
        # 수강할 수 있는 비전공 과목의 개수
        subject = 6 - major[i]
        if subject < non_major[i]:
            B += subject * 3
        else:
            B += non_major[i] * 3
        subject = 6

    if B >= 130 and A >= 66:
        print("Nice")
    else:
        print("Nae ga wae")