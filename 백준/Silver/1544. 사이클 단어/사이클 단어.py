import sys
input = sys.stdin.readline

n=  int(input())
cycle_set = set()

for _ in range(n):
    s = input().rstrip()
    # 모든 회전형 중 사전순으로 가장 작은 것을 대표값으로 사용
    min_cycle = min(s[i:] + s[:i] for i in range(len(s)))
    cycle_set.add(min_cycle)

print(len(cycle_set))