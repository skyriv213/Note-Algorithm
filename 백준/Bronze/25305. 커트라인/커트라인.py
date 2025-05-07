n,k = map(int, input().split())
score = list(map(int, input().split()))
print(sorted(score, reverse=True)[k-1])
