print("피라미드 높이를 입력하시오 :")
h = int(input())
s = []
'''
고려해야할 점
띄어쓰기 간격 만들기
숫자는 2의 배수로 증가 후 증감

'''
for i in range(1,h+1):
    s = [x *2 + 1 for x in range(0,i)]
    sr = sorted(s,reverse=True)
    sr.pop(0)
    s.extend(sr)
    print("  "*(h-i),end="")
    for j in s:
        print(j,end=" ")
    print("")
