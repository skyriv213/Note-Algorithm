'''
리스트 슬라이싱 startday를 포함하여 리스트를 다시 월요일부터 시작으로 변경, 주말은 상관없으니 리스트에서 제거
res = timelogs[i][8-startday:]+timelogs[i][:6-startday]

schedules 길이 회전 - for


'''

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        weekdays = [(startday - 1 + j) % 7 for j in range(7)]
        weekdays = [j for j in range(7) if weekdays[j] < 5]
        
        # 평일 출근 기록만 추출
        res = [timelogs[i][j] for j in weekdays]        
        hour,minute = schedules[i]//100, schedules[i]%100+10
        
        if minute>=60:
            hour+=1
            minute=minute-60
            time = hour*100+minute
        else:
            time = hour*100+minute
        if all(x <= time for x in res):
               answer+=1
                
                
    return answer