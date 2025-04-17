'''
1. s를 리스트로 분해
2. 각 문자안에 해당 skip부분의 문자 존재 시 다음 문자로 건너 뜀
3. z를 넘어가는 경우 a로 돌아옴. 이때 넘어가는 경우 길이로 나눈 나머지가 해당 문자의 인덱스
'''

def solution(s, skip, index):
    answer = ''
    alpha = [chr(w) for w in range(ord('a'),ord('z')+1) if chr(w) not in skip]
    for i in s:
        answer +=alpha[(alpha.index(i)+index) % len(alpha)]
        
    return answer