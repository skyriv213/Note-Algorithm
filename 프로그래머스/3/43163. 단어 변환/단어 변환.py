from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    queue = deque([(begin,0)])
    visit = set([begin])
    while queue:
        cu, tr = queue.popleft()
        if cu == target:
            return tr
        for word in words:
            if word not in visit:
                diff = 0
                for i in range(len(cu)):
                    if cu[i] != word[i]:
                        diff +=1
                if diff ==1:
                    queue.append((word, tr+1))
    return answer