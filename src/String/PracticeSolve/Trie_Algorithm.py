# 입력이 되는 문자열을 트리의 형태로 만들어서 빠르게 문자열 검색을 하는 알고리즘
#
# 문자열을 검색하는 문제에서 입력되는 문자열이 많을 경우 사용
#     빠른 시간복잡도로 검색엔진 사이트에서 자동완성 기능으로 사용
#
# 1 ) 노드를 이용한 Tree 형태로 이루어짐
# 2 ) 문자열의 끝을 알리는 flag 존재
#

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        cur_node = self.root # 처음 루트로 잡기
        for c in s:
            if c not in cur_node: # c가 해당 노드안에 존재하지않으면
                cur_node[c] ={} # 새로운 루트를 만든다 표현
            cur_node = cur_node[c]
        cur_node["*"] = s # 끝났다는 표시

    def search(self, s):
        cur_node = self.root
        for c in s:
            if c in cur_node:
                cur_node = cur_node[c]
            else:
                return False # 존재하지않으면 False 반환

        return "*" in cur_node # "*"가 있다면 그 문자로 끝나는 단어 존재재
