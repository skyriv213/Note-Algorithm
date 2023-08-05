def solution(progresses, speeds):
    answer = []
    # 작업이 걸리는 날을 미리 계산
    temp = [100 - i for i in progresses]  # 남은 퍼센테지를 계산
    for i in range(len(speeds)):
        t = temp[i] // speeds[i]
        if temp[i] > t * speeds[i]:  # 남은 퍼센테지가 임시값*속도이면
            t += 1
        temp[i] = t  # 아닐 경우

    idx = 0

    # 기준일을 지정
    # 날짜를 순회하면서 기준일과 비교
    # 기준일과 비교시 기준일보다 큰 경우
    # 해당 비교를 종료하고 answer 배열에 앞에 횟수가 세어진 숫자를 answer에 기입
    # 이때 기준일은 기준일보다 큰 경우로 변경

    for i in range(len(temp)):  # 날짜를 돌면서
        if temp[idx] < temp[i]:
            answer.append(i - idx)
            idx = i

    answer.append(len(temp) - idx)


    return answer