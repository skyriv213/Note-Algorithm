'''
속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
'''

def solution(genres, plays):
    answer = []
    cnt ={}
    music ={}
    for i, (g, p) in enumerate(zip(genres, plays)):
        cnt[g] = cnt.get(g, 0) + p
        music.setdefault(g, []).append((p, i))

    
    cnt = sorted(cnt, key = lambda x: cnt[x], reverse=True)
    
    for m in cnt:
        song = sorted(music[m], key = lambda x :(-x[0],x[1]))
        answer.extend([idx for _ , idx in song[:2]])

    return answer