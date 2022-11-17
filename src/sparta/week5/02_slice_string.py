input = "abcabcabcabcdededededede"

'''
문자열의 길이 가져오기 - 앞에서부터 해당 문자열을 잘라서 비교를 하기에 문자열 길이의 절반까지만 비교
문자열 비교를 하면서 길이를 비교하기 위한 리스트 필요
문자열 길이 절반만큼의 반복문 시행
이때 반복문을 진행하면서 반복문의 길이 절반만큼 앞에서 문자열 자르기 시행 후 splited라는 리스트에 넣어주기
문자열을 자르는 반복문을 진행할 경우 sp를 기준으로 또한 반복문을 진행 
그리고 문자열의 경우 최소 한번은 반복이 되므로 cnt 초기값을 1이라고 지정
반복문을 진행. 이때 반복문은 1부터 splited의 길이까지만 진행 
prev, cur 변수 선언, 이때 
'''


def string_compression(string):
    n = len(string)
    compression = []
    for sp in range(1, n // 2 + 1):
        compressed = ""
        splited = [
            string[i:i + sp] for i in range(0, n, sp)
        ]
        cnt = 1

        for j in range(1, len(splited)):
            # 문자열대로 잘려진 배열에서 prev / cur이 동일하다면
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                # 1을 더해준다
                cnt += 1
            else:
                # 동일하지 않다면
                if cnt > 1:
                    # 만약 cnt가 1보다 큰상황에서는 cnt + prev로 표현
                    compressed += (str(cnt) + prev)
                else:
                    # 1과 같다면 문자열 변수에 prev만 더해줄것
                    compressed += prev
                cnt = 1
        # 1보다 큰 cnt로 끝난 경우 해당 cnt와 문자열의, 나머지를 전부다 더해주기,splited의 마지막 원소는 나머지이기 때문
        if cnt > 1:
            compressed += (str(cnt) + splited[-1])
        else:
            # 아닌 경우 그냥 더해주기
            compressed += splited[-1]
            # 문자열의 길이 넣어주기
        compression.append(len(compressed))
    return min(compression)


print(string_compression(input))  # 14 가 출력되어야 합니다!
