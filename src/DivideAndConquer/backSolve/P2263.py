'''
n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다.
이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

3 - 노드의 갯수
1 2 3 - 인 오더
1 3 2 - 포스트 오더

트리의 모양
    2
1       3

left : 1
root : 2
right : 3

문제에서 요하는 답 - 프리 오더
2 1 3

풀기위한 방법 :


'''

n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))

p = [0 for _ in range(n)]
