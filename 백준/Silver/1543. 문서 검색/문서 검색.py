doc = input()
s = input()
# print(doc,s)
i,cnt= 0,0
while i < len(doc):
    temps =doc[i:i+len(s)]
    if s == temps:
        cnt+=1
        i+=len(s)
    else:
        i+=1

print(cnt)