def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for s in string:
        if s.isalpha():
            alphabet_occurrence_array[ord(s) - ord('a')] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))

input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    arr = find_alphabet_occurrence_array(string)
    a = max(arr)
    arr2 = []
    for i in range(0,26):
        if a == arr[i]:
            arr2.append(i)

    return arr2


result = find_max_occurred_alphabet(input)
for i in result:
    print(chr(i+ord('a')))
