'''
노드이다.
노드의 경우 앞에서 말한 바와 같이 데이터를 저장하는 인자와
다음 데이터를 받아오기 위한 정보가 있는 next로 구성이 되어있다.
처음 next값은 다음 노드의 정보를 원활하게 받아오기 위해 None으로 지정을 한다.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


'''
node를 이어서 만드는 링크드 리스트 자료구조이다.
'''


class LinkedList:
    # 생성자
    def __init__(self, value):
        # 연결리스트의 가장 처음에 오는 노드는 head라고 지정을 한다.
        self.head = Node(value)

    # ------------------------------------------------------------------------------------------------------------------

    # 1. append : 추가하고자 하는 값을 받아와서 제일 마지막 노드에 넣어 연결을 하는 메서드
    # 해당 메서드의 경우 시간복잡도는 o(n)이다. while을 통해 현재 리스트 안에 저장된 데이터의 갯수에 따라 반복문을 진행하기 때문이다.
    def append(self, value):
        # cur을 선언해준다. cur의 경우 head, 즉 처음부터 시작을 한다
        cur = self.head

        # cur의 next가 None이 아닐 때까지 반복을 하며 cur의 경우 반복분이 진행될 때마다 다음 cur로 넘어가게 된다.
        while cur.next is not None:
            cur = cur.next
        # 만약 반복문이 종료가 되면 해당 경우에는 현재 가지고 있는 cur의 next가 None이라는 의미이며
        # 이 경우 Node를 새로 선언하고 해당 노드를 cur의 next로 지정을 해준다.
        cur.next = Node(value)

    # ------------------------------------------------------------------------------------------------------------------

    # 2. print_all : 해당 리스트의 데이터 값을 모두 보여주는 메서드
    # 해당 메서드의 경우 시간복잡도는 o(n)이다. while을 통해 현재 리스트 안에 저장된 데이터의 갯수에 따라 반복문을 진행하기 때문이다.
    def print_all(self):
        # cur을 선언하고 이는 현재 cur의 head이다.
        cur = self.head
        # 현재 cur이 아무것도 존재하지 않을 때 까지만 반복을 한다.
        while cur is not None:
            # cur.data를 출력하고, cur을 cur의 next로 선언한다
            print(cur.data)
            cur = cur.next

    # ------------------------------------------------------------------------------------------------------------------

    # 3. get_node : n번째 리스트의 값을 반환하는 메서드
    # 해당 메서드의 경우 시간복잡도는 o(index)이다. while을 통해 현재 리스트 탐색의 갯수에 따라 반복문을 진행하기 때문이다.
    def get_node(self, index):
        node = self.head
        # index와 비교를 위해 count 선언
        count = 0
        while count < index:  # 해당 반복문은 count가 index보다 작을 때까지만 반복을 하며
            node = node.next  # 노드의 상태를 반복문이 진행할 때마다 다음 노드를 가져온다
            count += 1
        return node  # index값에 맞는 노드를 리턴하여 보여준다

    # ------------------------------------------------------------------------------------------------------------------

    # 4. add_node : 원하는 자리에 원하는 값을 넣는 메서드
    def add_node(self, index, value):
        new_node = Node(value) # 새로운 노드 생성
        # 다만 new_node가 원하는 index가 처음인 경우
        if index == 0:
            # new node의 next를 현재 head로 지정한다. 그리고 다음 현재 head값을 new_node로 지정한다
            new_node.next = self.head
            self.head = new_node
            return

        # 원하는 index에 해당 노드를 넣어 값을 지정하고 보관하고 싶은 경우
        # index - 1 번째의 노드를 가져오고 해당 노드의 next에 새로 생성한 new_node를 넣어줘야 제 위치를 찾아갈수 있다.
        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    # ------------------------------------------------------------------------------------------------------------------

    # 5. delete_node : 인덱스를 입력받고 그 인덱스의 노드를 제거하는 메서드
    def delete_node(self, index):
        # 만약 지우고자 하는 index가 0이라면
        if index == 0:
            # 현재 해드는 현재 해드의 다음으로 덮어씌워진다
            self.head = self.head.next
        # index -1의 노드를 get_node 메서드를 통해 가져온다
        node = self.get_node(index - 1)
        # 그리고 나서 그 노드의 다음의 다음 노드를 가져오는 정보를 현재 노드로 이어붙여준다
        node.next = node.next.next

