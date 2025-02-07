'''
아이디어 : 분할정복
- 2차원 배열을 한번에 처리하는 대신, 배열을 작은 구역으로 분할하여 각 구역이 모두 동일한 값으로 이루어져있는지 검사
- 동일하지 않다면 해당 영역을 4개의 작은 영역으로 분할, 검사

종료 조건
- 각 영역이 동일한 값으로 채워져 있으면 해당 영역을 더 이상 분할하지 않고, 해당 값이 무슨 값인지 확인 후 answer에서 증가



quad : 재귀함수
입력 변수 : arr : 배열, x,y : 시작좌표, n : 구역의 크기
quad(arr,x,y,n)
quad(arr,x+n,y,n)
quad(arr,x,y+n,n)
quad(arr,x+n,y+n,n)

'''

def quad(arr,x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if(arr[i][j]!=arr[x][y]):
                n//=2
                quad(arr,x,y,n)
                quad(arr,x+n,y,n)
                quad(arr,x,y+n,n)
                quad(arr,x+n,y+n,n)
                return
    answer[arr[x][y]]+=1
                

def solution(arr):
    global answer 
    answer = [0,0]
    quad(arr, 0,0,len(arr))
    return answer