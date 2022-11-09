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


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    # sum1 = ''
    sum1 = sum_link(linked_list_1)

    sum2 = sum_link(linked_list_2)
    return sum2+sum1


def sum_link(linked_list_1):
    sum1 = 0
    head_1 = linked_list_1.head
    while head_1 is not None:
        # sum1 += str(head_1.data)
        sum1 = sum1 * 10 + head_1.data
        head_1 = head_1.next
    return sum1


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
