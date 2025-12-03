n = int(input())
chicken = list(map(int, input().split()))
target = int(input())


def sortchicken(chicken):
    if len(chicken) == n//target:
        chicken.sort()
        return chicken
    half = len(chicken) // 2
    left = sortchicken(chicken[:half])
    right = sortchicken(chicken[half:])
    return left +right
print(*sortchicken(chicken))