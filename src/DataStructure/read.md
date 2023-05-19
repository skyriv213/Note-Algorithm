우선순위 큐

우선 순위 큐에 대해 정리해 드리겠습니다. 우선 순위 큐는 일반적인 큐와 비슷한 선형 자료구조이지만, 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나오는 것을 말합니다1. 우선 순위 큐는 다음과 같은 특징을 가집니다.

모든 항목에는 우선순위가 있습니다.
우선 순위가 높은 요소는 우선 순위가 낮은 요소보다 먼저 queue에서 제외됩니다.
두 요소의 우선 순위가 같으면 queue의 순서에 따라 제공됩니다.
우선 순위 큐는 다음과 같은 기본 동작을 지원합니다.

enqueue() - queue에 새 요소를 삽입합니다.
dequeue() - queue에서 최대 우선순위 요소를 삭제하고 그 값을 반환합니다.
peek() - queue에서 최대 우선순위 요소를 반환합니다.
우선 순위 큐의 구현 방식에는 배열, 연결 리스트, 힙이 있습니다. 각 구현 방식의 시간 복잡도는 다음과 같습니다1.

구현 방법	enqueue()	dequeue()
배열 (unsorted array)	O(1)	O(N)
연결 리스트 (unsorted linked list)	O(1)	O(N)
정렬된 배열 (sorted array)	O(N)	O(1)
정렬된 연결 리스트 (sorted linked list)	O(N)	O(1)
힙 (heap)	O(logN)	O(logN)
*N : 노드 수

힙 방식이 최악의 경우라도 O(logN)을 보장하기 때문에 일반적으로 힙을 가지고 구현을 합니다. 힙에 대한 내용은 다른 문서를 참고하시기 바랍니다2.

우선 순위 큐의 요소의 구조는 다음과 같이 나타낼 수 있습니다.

struct node {
  int data;
  int priority;
}
우선 순위 큐의 사용 예시는 다음과 같습니다3.

import java.util.PriorityQueue;

public class Main {
  public static void main(String[] args) {
    // 우선순위 큐 선언
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    
    // 우선순위 큐에 값을 넣는다.
    pq.add(5);
    pq.add(3);
    pq.add(6);
    pq.add(1);
    pq.add(2);
    
    // 우선순위 큐 출력
    // 큐가 비어있지 않다면 무한반복 비어있다면 반복문을 실행하지 않는다
    while(!pq.isEmpty()) {
      // 큐의 제일 앞의 부분의 값 가져오기
      int temp = pq.poll();
      System.out.print(temp + " ");
    }
    
    // 출력 결과
    // 1 2 3 5 6
  }
}
넣는 순서와 상관없이 작은 값이 제일 먼저 나오게 됩니다. 이는 기본적으로 자바에서 제공하는 비교연산자가 작은 값이 높은 우선순위를 갖도록 정의되어 있기 때문입니다.