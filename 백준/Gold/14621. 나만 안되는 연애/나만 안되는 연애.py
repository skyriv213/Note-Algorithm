
'''
나만 안되는 연애

n,m = 학교 수, 도로 개수
주어진 학교의 성별 구분

u,v,d -> u,v가 연결되며 거리는 d가 됨
앱의 경로 길이를 출력

'''

# 서로소집합
def find (love, a):
    if love[a] != a:
        love[a] = find(love, love[a])
    return love[a]

def union(love, a,b):
    a = find(love, a)
    b = find(love, b)
    if a<b:
        love[b] = a
    else:
        love[a] = b

n,m = map(int, input().split())
res =0
edges =[]
men = []
women =[]

# 자기 자신으로 초기화
love = [i for i in range(n+1)]


# 남녀 대학교 구분
s = input().split()
for i in range(len(s)):
    if s[i] == "M":
        men.append(i+1)
    else:
        women.append(i+1)

for i in range(m):
    u,v,d = map(int, input().split())
    if (u in men and v in women) or (u in women and v in men) :
        edges.append((d,u,v))

edges.sort()
cnt = 0

for e in edges:
    d,u,v = e
    if find(love,u) != find(love,v):
        union(love,u,v)
        cnt+=1
        res+=d



# 출력 부분

print(res if cnt == n-1  else -1)
