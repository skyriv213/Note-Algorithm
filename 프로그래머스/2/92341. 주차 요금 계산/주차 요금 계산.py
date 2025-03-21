from datetime import datetime
import math

def solution(fees, records):
    # 차량별 주차 시간을 저장할 딕셔너리
    car_time = {}
    
    # 차량별 입차 시간을 저장할 딕셔너리
    car_in_time = {}
    
    for record in records:
        time, car_num, status = record.split()
        
        # 시간을 분 단위로 변환
        time_min = datetime.strptime(time, "%H:%M").hour * 60 + datetime.strptime(time, "%H:%M").minute
        
        if status == "IN":
            # 입차 시간 저장
            car_in_time[car_num] = time_min
        else:
            # 출차 시간으로부터 주차 시간 계산
            if car_num not in car_time:
                car_time[car_num] = time_min - car_in_time[car_num]
            else:
                car_time[car_num] += time_min - car_in_time[car_num]
            
            # 입차 시간 삭제
            del car_in_time[car_num]
    
    # 입차 후 출차 내역이 없는 차량 처리
    for car_num, in_time in car_in_time.items():
        if car_num not in car_time:
            car_time[car_num] = 1439 - in_time  # 23:59에 출차된 것으로 간주
        else:
            car_time[car_num] += 1439 - in_time
    
    # 주차 요금 계산
    result = []
    for car_num in sorted(car_time.keys()):
        time = car_time[car_num]
        if time <= fees[0]:
            result.append(fees[1])
        else:
            result.append(fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3])
    
    return result


