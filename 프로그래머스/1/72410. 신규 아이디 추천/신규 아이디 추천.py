import re
def solution(new_id):
    answer = ''
    # 1단계 : lower()
    new =  new_id.lower()
    # 2단계 : 정규식
    new =  re.sub(r'[^a-z0-9\-\_\.]', '', new)
    # 3단계 : for문으로 .이 연속인지 확인
    while '..' in new:
        new = new.replace('..', '.')

    # 4단계 : if 문으로 .이 1, -1에 존재하면 제거
    new = new.strip(".")

    new = list(new)

    # 5단계 : 빈 문자열이면 new_id에 a 대입
    if len(new) == 0:
        new.append("a")
    print(new)

    # 6단계 : len >=16 -> new_id[:16],if -1 == . : replace('.','')
    if len(new)>=16:
        new = new[:15]
        if new[-1] ==".":
            new.pop()
    print(new)

    # 7단계 : if len <=2, new_id += new_id[-1]*(3-len(new_id))
    if len(new)<=2:
        new.append(new[-1]*(3-len(new)))
    print(new)

    return ''.join(new)