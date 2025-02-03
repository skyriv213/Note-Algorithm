import heapq

def solution(k, score):
    answer = []
    queue = []
    for i in score:
        '''
        if 리스트의 길이 k까진 모든 원소 힙 삽입
        else k 번째 이후 최소원소, score 비교 
            if k가 더 높은 경우:
                최소원소 제외, k 삽입
            else k가 더 낮은 경우:
                최소원소 유지
        value = heapq의 최소원소
        answer.append(value)
        
        '''
        if len(queue) < k:
            heapq.heappush(queue, i)
            answer.append(heapq.heappop(queue))
            heapq.heappush(queue,answer[-1])
        else:
            val = heapq.heappop(queue)
            if val < i:
                heapq.heappush(queue, i)
                answer.append(heapq.heappop(queue))
                heapq.heappush(queue,answer[-1])
            else:
                heapq.heappush(queue, val)
                answer.append(heapq.heappop(queue))
                heapq.heappush(queue,answer[-1])



    return answer