n = str(input())
print("LUCKY" if sum(list(map(int,n[:len(n)//2]))) == sum(list(map(int,n[len(n)//2:]))) else "READY")
