def find_team(team, a):
    if team[a] != a:
        team[a] = find_team(team, team[a])
    return team[a]


def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)

    if a < b:
        team[b] = a
    else:
        team[a] = b


n, m = map(int, input().split())
team = [0] * (n + 1)

for i in range(0, n + 1):
    team[i] = i

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_team(team, a, b)
    elif oper == 1:
        if find_team(team, a) == find_team(team, b):
           print('yes')
        else:
            print('no')
