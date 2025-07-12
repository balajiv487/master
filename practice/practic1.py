def count_frequency(l):
    f={}
    for i in l:
        f[i]=f.get(i,0)+1
    return f
l=[1,2,2,3,3,3,4,4,4,4]

print(count_frequency(l))

s = "banana"
print(s.count('a'))