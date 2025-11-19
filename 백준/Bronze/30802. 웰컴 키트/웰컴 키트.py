n = int(input()) # 참가자의 수

# S M L XL XXL XXXL
size = list(map(int,input().split()))

# 티셔츠, 펜의 최소 몇묶음 주문 갯수,
t, p= map(int,input().split())

ans1 = 0

for i in size:
  if (i//t)*t <i:
    ans1+=(i//t)+1
  else:
      ans1+=i//t



print(ans1)
print(n//p, n%p)