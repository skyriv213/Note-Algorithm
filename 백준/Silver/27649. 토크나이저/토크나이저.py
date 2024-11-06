s = input()
li = []
ex = set(["<", ">", "(", ")", " "])
plus = set(["&&", "||"])
op1 = set(['', ' '])
op2 = set(["&", "|"])
token = ''
deli = ''

'''
for문 s 돌리기
1. s[i]가 ex에 있는지 확인
    존재 시 해당 s[i], token는 li에 추가
2. deli + s[i]가 plus에 있는지 확인
    존재시 token,deli를 li에 추가
3. 둘 다 아닐 경우
    if s[i]가 & ,| 인 경우
        deli += s[i]
    else :
        token += s[i]
마지막 token값 li 저장
li for 문 돌리기
    만약 돌렸을때 공백이면 출력 x
    
'''

for i in range(len(s)):

    if s[i] in ex:
        li.append(token)
        li.append(s[i])
        token = ''
    elif deli + s[i] in plus:
        li.append(token)
        li.append(deli + s[i])
        deli = ''
        token = ''
    else:
        if s[i] in op2:
            deli += s[i]
        else:
            token += s[i]

li.append(token)

res = " ".join([i for i in li if i.strip()])

print(res.rstrip())
