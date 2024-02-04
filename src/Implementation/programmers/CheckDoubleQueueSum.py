from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    cnt = 0

    for i in range((len(queue1) + len(queue2) * 2)):
        if sum1 > sum2:
            moved_item = queue1.popleft()
            queue2.append(moved_item)
            sum1 -= moved_item
            sum2 += moved_item
            cnt += 1
        elif sum1 < sum2:
            moved_item = queue2.popleft()
            queue1.append(moved_item)
            sum1 += moved_item
            sum2 -= moved_item
            cnt += 1
        else:
            break

    if sum1 == sum2:
        return cnt
    else:
        return -1