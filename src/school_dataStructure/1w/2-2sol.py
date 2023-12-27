import os
import random

min ,max ,cnt, answer = 0,99, 0,random.randint(0,100)

for i in range(10):
    cnt+=1
    print(
        "숫자를 입력하세요(범위 : ", min,"~",max,")"
    )
    guess = int(input())
    if guess > max:
        print("숫자를 다시 입력해주세요")
        guess = int(input())
    elif min>guess:
        print("숫자를 다시 입력해주세요")
        guess = int(input())

    if min<=guess<answer:
        min = guess
        print("아닙니다. 더 큰 숫자입니다")
    elif answer == guess:
        print("정답입니다",cnt,"번만에 맞췄습니다" + "\n" + "게임이 끝났습니다")
        break
    else:
        max=guess
        print("아닙니다. 더 작은 숫자 입니다")

