'''
문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

split()으로 쪼갤 때 기본 공백말고 직접 공백으로 체크해주기
직접 공백으로 체크하여 혹여 공백이 연달아 나와도 공백으로도 배열이 쪼개질수 있도록
'''


def solution(s):
    answer = ''
    new_list = s.split(' ')
    print(new_list)
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]

s="try    hello world"
print(solution(s))