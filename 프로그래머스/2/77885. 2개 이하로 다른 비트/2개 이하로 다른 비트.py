def solution(numbers):
    answer = [] # x보다 크고 x와 비트가 1~2개 다른 수 중에서 제일 작은수
        
    for i in numbers:
        if i %2 ==0:
            answer.append(i+1)
        else:
            num1 = '0'+bin(i)[2:]
            zeroIdx = num1.rfind('0')
            num1 = list(num1)
            num1[zeroIdx] ='1'
            num1[zeroIdx+1] = '0'
            answer.append(int(''.join(num1),2))
            
            
                
    return answer