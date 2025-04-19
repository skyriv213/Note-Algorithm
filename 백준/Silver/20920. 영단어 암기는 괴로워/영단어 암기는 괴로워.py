import sys
input = sys.stdin.readline

n,m = map(int, input().split())
word = {}

for i in range(n):
    s = input().rstrip()
    if len(s) >= m:
        word[s] = word.get(s, 0) + 1
    else:
        pass


word = sorted(word, key=lambda x: (-word[x],-len(x),x) )
for i in word:
    print(i)