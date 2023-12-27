def solution(players, callings):
    race = {}  # 현재 경기의 순위

    for i, p in enumerate(players):
        race[p] = i  # 인원과 등수

    for c in callings:
        # 기존 index()를 race 딕셔너리로 사용
        # 해당 인물이 불렸다면, 앞의 인물과의 교환작업 -> if문으로 확인했었지만 문제에서
        # players의 원소로만 이루어졌다고 말했기에 확인 작업 불필요
        idx = race[c]
        race[c] -= 1
        race[players[idx - 1]] += 1

        players[idx - 1], players[idx] = players[idx], players[idx - 1]

    return players