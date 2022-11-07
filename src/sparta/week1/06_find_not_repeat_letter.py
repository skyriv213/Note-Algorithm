input = "abadabac"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요
    arr = [0] * 26
    for s in string:
        if s.isalpha():
            arr[ord(s) - ord('a')] += 1
    for s in string:
        if arr[ord(s) - ord('a')] == 1:
            return s


result = find_not_repeating_character(input)
print(result)
