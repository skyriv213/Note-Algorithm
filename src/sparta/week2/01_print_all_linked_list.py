class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return


        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

# node = Node(3)
#
# first_node = Node(4)
# node.next = first_node
#
# print(node.data)
# print(node.next.data)

link = LinkedList(3)
link.append(4)
link.append(5)
link.print_all()

