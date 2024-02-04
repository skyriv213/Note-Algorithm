def solution(x, y, n):
    def recur(x, y, n, cnt, numlist):
        if x == y:
            return numlist.append(cnt)
        elif x > y:
            return 1e9
        else:
            recur(x + n, y, n, cnt + 1, numlist)
            recur(x * 2, y, n, cnt + 1, numlist)
            recur(x * 3, y, n, cnt + 1, numlist)

    numlist = [1e9]
    recur(x, y, n, 0, numlist)
    answer = min(numlist)
    if answer == 1e9:
        return -1
    else:
        return answer


def solution(x, y, n):

    dp = [1e9] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == 1e9:
            continue

        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)

        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)

        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    if dp[y] == 1e9:
        return -1

    return dp[y]
