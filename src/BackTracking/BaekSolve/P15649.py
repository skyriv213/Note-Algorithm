n, m = map(int, input().split())

s = []

def dfs():
    # 배열의 길이가 m이 되는 경우 해당 리스트 내의 숫자들을 join 메서드를 활용하여 출력 후 해당 dfs 종료
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    # for 문으로 반복
    for i in range(1, n + 1):
        # 만약 i가 리스트 s안에 존재하지 않는다면 삽입을 해주고 dfs를 호출한다.
        # 해당 dfs가 출력 된 후 가장 뒤에 들어온 i를 pop하여 제거해준다.
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()