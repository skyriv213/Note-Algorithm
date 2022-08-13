'''
KMP 알고리즘 

시간복잡도 O(n)

KMP 알고리즘은 해당 문자열의 Degenerate Pattern을 이용하여 빠른검색을 하도록 만든 알고리즘

Degenerate pattern
전체의 어떤 패턴 속에 있는 작은 패턴이 한 번 이상 반복되는 현상

Prefix - 접두어 / Suffix - 접미어
LPS - Longest proper prefix which is suffix 
prefix 와 suffix가 같은 경우 가장 길이가 긴 경우를 의미

'''

# 브루트 포스 탐색 시간복잡도 O(n*m)
target = 'ABC'
text = 'ABABCA'

for i in range(len(text) - len(target)):
    for j in range(len(target)):
        if text[i + j] == target[j]:
            j += 1
        else:
            break

    print('Identified')
    break

pat = 'ABXAB'

# 자기 탐색으로 인해 이 경우에는 i는 무조건 다음인 1부터
def computeLPS(pat, lps):
    j = 0
    i = 1
    while i < len(pat):
        if pat[j] == pat[i]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1


def KMPSearch(txt, pat):
    i, j = 0, 0

    lps = [0 for _ in range(len(pat))]
    computeLPS(pat, lps)

    while i < len(txt):
        if txt[i] == pat[j]:
            i += 1
            j += 1
        elif txt[i] != pat[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        # 문자열의 존재 확인 시 return / 확인 이후에도 추가적인 탐색을 원한다면 j를 다시 원위치로 돌리는 j = lps[j-1]
        if j == len(pat):
            # return True
            # print("Found pattern at index " + str(i - j)) # 해당 예제에서 확인용
            j = lps[j - 1]


txt = 'ABXABABXAB'
pat = 'ABXAB'
KMPSearch(txt, pat)
