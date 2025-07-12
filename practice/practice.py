def sq_n(n):
    l=[]
    s=[]
    l= [i**2 for i in n]
    s.extend([l])
    return s

s=[2,3,4,5]
s.extend([6])
print(sq_n(s))