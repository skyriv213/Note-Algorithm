# '''
# 10초 전 이동 - prev
# 10초 후 이동 - next
# 오프닝 건너뛰기 - op_start <= 현재 위치 <= op_end -> 자동으로 op_end의 위치로 이동

# 오프닝 건너뛰기 - skip(pos, op_start, op_end)
# if op_start ≤ pos ≤ op_end return op_end

# 10초 전 이동 - mm:ss - 00:10
#     if pos < 00:10:
#         return 00:00
        
# 10초 후 이동 = mm:ss + 00:10
#     if video_len - pos < 00:10 :
#         return video_len


# 매 연산 마다 skip 실행

# '''

# def mT(time):
#     return check(time[:2]),check(time[3:])

# def check(tt):
#     if len(tt) == 1:
#         return "0"+tt
#     return tt

# def skip(pos, op_start, op_end):
#     mm,ss = mT(pos)
#     opm, ops = mT(op_start)
#     oem, oes = mT(op_end)
#     if int(opm) <= int(mm) <=int(oem) and int(ops) <=int(ss)<=int(oes):
#         return oem, oes
#     return mm,ss

# def prev(mm,ss):
#     if int(ss) < 10:
#         if mm == "00":
#             return "00","00"
#         else:
#             ss = str(60+int(ss)-10)
#             mm = str(int(mm)-1)
#             return mm,ss
#     else:
#         return mm,check(str(int(ss)-10))

# def next(mm,ss,video_len):
#     if int(ss) >50:
#         ss = check(str(int(ss)+10 - 60))
#         mm = str(int(mm)+1)
#     else:
#         ss = str(int(ss)+10)
#     cm, cs = mT(video_len)
#     if mm == cm and abs(int(cs)-int(ss))<10:
#         return cm, cs
#     return mm,ss
        
# def solution(video_len, pos, op_start, op_end, commands):
#     mm,ss=skip(pos, op_start, op_end)
#     for i in commands:
#         mm,ss=skip(mm+ss, op_start, op_end)
#         if i == "prev":
#             mm,ss = prev(mm,ss)
#             mm,ss = skip(mm+ss, op_start, op_end)
#         else:
#             mm,ss = next(mm,ss,video_len)
#     return mm+":"+ss

def mT(time):
    """ "mm:ss" 형태의 시간을 분과 초로 분리하여 반환 """
    mm, ss = map(int, time.split(":"))
    return mm, ss

def format_time(mm, ss):
    """ mm, ss를 두 자리 숫자로 변환하여 "mm:ss" 형식으로 반환 """
    return f"{mm:02}:{ss:02}"

def time_to_seconds(mm, ss):
    """ 분과 초를 총 초 단위로 변환 """
    return mm * 60 + ss

def seconds_to_time(seconds):
    """ 총 초 단위를 "mm:ss" 형식으로 변환 """
    mm, ss = divmod(seconds, 60)
    return format_time(mm, ss)

def skip(pos, op_start, op_end):
    """ 오프닝 구간을 건너뛰는 함수 """
    pos_sec = time_to_seconds(*mT(pos))
    op_start_sec = time_to_seconds(*mT(op_start))
    op_end_sec = time_to_seconds(*mT(op_end))

    if op_start_sec <= pos_sec <= op_end_sec:
        return seconds_to_time(op_end_sec)
    return pos

def prev(pos):
    """ 10초 전으로 이동하는 함수 """
    pos_sec = max(0, time_to_seconds(*mT(pos)) - 10)
    return seconds_to_time(pos_sec)

def next(pos, video_len):
    """ 10초 후로 이동하는 함수 """
    pos_sec = time_to_seconds(*mT(pos))
    video_len_sec = time_to_seconds(*mT(video_len))

    new_pos_sec = min(video_len_sec, pos_sec + 10)
    return seconds_to_time(new_pos_sec)

def solution(video_len, pos, op_start, op_end, commands):
    pos = skip(pos, op_start, op_end)  # 초기 위치 체크
    
    for command in commands:
        pos = skip(pos, op_start, op_end)  # 이동 전 skip 검사

        if command == "prev":
            pos = prev(pos)
            pos = skip(pos, op_start, op_end)  # 이동 후 skip 검사
        elif command == "next":
            pos = next(pos, video_len)

    return pos
