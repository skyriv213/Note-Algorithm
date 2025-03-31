from itertools import product

def solution(word):
    v =['A','E','I','O','U']
    
    dic =[]
    
    for l in range(1,6):
        for c in product(v, repeat=l):
            dic.append(''.join(c))
    dic.sort()
    
    return dic.index(word)+1