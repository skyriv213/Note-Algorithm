import heapq

# def solution(operations):
#     answer = []
#     for i in operations:
#         o, n = i.split()
#         if o == "I":
#             heapq.heappush(answer,int(n))
#         else:
#             if len(answer) ==0 :
#                 continue
#             if n == "1":
#                 answer.pop()
#             else:
#                 heapq.heappop(answer)
#     if len(answer) == 0:
#         return [0,0]
#     elif len (answer) ==1:
#         return[max(answer),0]
#     else:
#         return [max(answer),min(answer)]
#     return answer
def solution(operations):
    maxH =[]
    minH = []
    for i in operations:
        o,n = i.split()
        n = int(n)
        if o == "I":
            heapq.heappush(maxH,-n)
            heapq.heappush(minH,n)
        else:
            if not minH:
                continue
            if n == 1:
                maxV = -heapq.heappop(maxH)
                minH.remove(maxV)
                heapq.heapify(minH)
            else:
                minV = heapq.heappop(minH)
                maxH.remove(-minV)
                heapq.heapify(maxH)
    if not minH:
        return [0,0]
    return [-maxH[0],minH[0]]