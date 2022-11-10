input = "abcba"


def is_palindrome(string):
    for i in range(len(string)):
        if string[i] != string[len(string)-1 - i]:
            return False
    return True


print(is_palindrome(input))
