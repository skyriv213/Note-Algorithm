'''
1. 데이터를 입력받는다
2. 글자의 크기를 비교하면서 진행
3. 글자의 크기는 최대 주어진 문자열의 길이 절반 = 동일한 크기로 문자를 쪼개야하기때문
4. 압축시킬수 있는 문자열의 최소 길이 출력
'''
# 데이터의 입력
s = input()
# 결과값 비교를 위해 최대 길이를 1로 쪼개졌다는 가정하에 s의 길이로 설정
res = len(s)
# 문자열을 쪼개는 최대 길이 파악을 위해 문자열의 길이 절반까지 비교
for i in range(1, len(s) // 2):
    # 마지막 res와 비교를 위한 임시값 tmp 설정
    tmp = ''
    # 잘라진 문자열의 앞뒤 비교를 위해 prev 설정
    prev = s[0:i]
    # 이때 같은 문자가 존재 시 앞에 체크를 하기위한 cnt 설정
    cnt = 1
    # i의 값 다음 값과 비교, 즉 첫번쨰 반복문은 잘라지는 범위를 구하기 위한 반복문
    # 두번째 반복문은 그 뒤의 문자열과 비교를 위한 반복문
    # 따라서 j는 i부터 시작하며, 크기는 i만큼 커진다
    for j in range(i, len(s), i):
        # 잘라진 범위가 s의 다음 크기와도 같다면 cnt+=1을 진행
        if prev == s[j:j + i]:
            cnt += 1
        # 만약 아니라면 cnt가 2 이상일 때
        else:
            # cnt를 문자로 변환 및 비교 대상 문자를 붙여서 tmp에 저장
            if cnt >= 2:
                tmp += str(cnt) + prev
            # cnt가 1일 경우 prev만 붙여준다
            else:
                prev
            # 똑같은 크기로 prev, 숫자 1로 cnt 다시 정의
            prev = s[j:j + i]
            cnt = 1
    # 위의 과정으로 다시 남은 숫자들 반복
    if cnt >= 2:
        tmp += str(cnt) + prev
    else:
        prev
    # 마지막 최솟값 비교 후 전달
    res = min(res, len(tmp))

print(res)
