def merge_list(l:list ,m:list):
    m=sorted(l+m)
    return m

l=[1,3,2,0]
m=[5,3,4,0]

print(merge_list(l,m))