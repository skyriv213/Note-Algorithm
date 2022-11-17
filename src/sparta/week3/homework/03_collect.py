s = "(())()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    s = []
    for i in range(len(string)):
        if string[i] == '(':
            s.append('(')
        if string[i] == ')' and len(s) > 0:
            s.pop()
    if len(s) > 0:
        return False
    else:
        return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
