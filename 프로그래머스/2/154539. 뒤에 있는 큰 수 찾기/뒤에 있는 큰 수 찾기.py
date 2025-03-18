def solution(numbers):
    
    # answer = []
#     maxNum = max(numbers)
#     for i in range(len(numbers)-1):
#         if numbers[i] == maxNum:
#             answer.append(-1)
#         else:
#             for j in numbers[i+1:]:
#                 if numbers[i]<j:
#                     answer.append(j)
#                     break
#                 if j == max(numbers[i+1:]):
#                     answer.append(-1)

#     answer.append(-1)
#     for i, num in enumerate(numbers):
#         for j in numbers[i + 1:]:
#             if num < j:
#                 answer.append(j)
#                 break
#         else:
#             answer.append(-1)
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer

