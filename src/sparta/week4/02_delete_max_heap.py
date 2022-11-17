class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 힙의 최대 높이는 o(log n)이며 최대 반복 횟수도 o(log(n)) 시간복잡도는 이와 같다
    def delete(self):
        # 구현해보세요!
        self.items[1], self.items[-1] = self.items[-1], self.items[1]  # 처음과 끝을 교환
        prev_max = self.items.pop() # prev_max값 생성 및 맥스힙에서 제거
        cur_index = 1 # 현재 인덱스는 1 지정

        while cur_index <= len(self.items) - 1: # 현재 인덱스에서 마지막 인덱스 -1까지 실행, 마지막인덱스는 사라진 상황
            # 자식 노드 찾아가는 코드
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            # 가장 큰 인덱스를 일단 현재 인덱스로 지정
            max_index = cur_index

            #만약 비교대상의 인덱스가 현재 힙의 길이 -1 보다 작고 또한 비교할 때 경우가 더 큰 경우 인덱스 max_idx 교환
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            # 만약 max_idx = cur_idx 일시 while break
            if max_index == cur_index:
                break

            # 스와이프
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            # 현재 인덱스를 가장 큰값의 인덱스 값을 가진 값을 스와이프하여 위치 찾아가기
            cur_index = max_index
        # 처음 선언한 max값
        return prev_max


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]