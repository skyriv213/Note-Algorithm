class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # 맨 뒤에 데이터 추가하기
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():  # 만약 비어있다면,

            self.head = new_node  # head 에 new_node를
            self.tail = new_node  # tail 에 new_node를 넣어준다.
            return

        self.tail.next = new_node
        self.tail = new_node

    # 맨앞 데이터 뽑기
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    # 맨 앞의 데이터 보기
    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    # 큐가 empty 여부 확인
    def is_empty(self):
        return self.head is None


queue = Queue()
queue.is_empty()
queue.enqueue(3)
print(queue.peek())
queue.dequeue()
queue.enqueue(34)
print(queue.peek())
queue.enqueue(35)
print(queue.peek())

queue = []
queue.append(5)
queue.popleft()