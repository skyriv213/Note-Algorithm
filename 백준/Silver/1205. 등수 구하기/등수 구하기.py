

n, score, p =map(int, input().split())
if n == 0:
    print(1)
else:
    rank = list(map(int, input().split()))
    if n ==p and score<= rank[-1]:
        print(-1)
    else:
        rank.append(score)
        rank.sort(reverse=True)
        print(rank.index(score)+1)
