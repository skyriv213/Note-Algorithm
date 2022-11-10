class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # cur = self.head
        # length = 0
        # # 리스트의 전체 길이 찾기
        # while cur is not None:
        #     length += 1
        #     cur = cur.next
        #
        # end = length - k
        # cnt = 0
        # cur = self.head
        # for i in range(end):
        #     cur = cur.next
        # return cur

        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
