def move_to_end(l,e):
    print(l)
    print(e)
    cnt=l.count(e)
    print(cnt)
    l=[ i for i in l if i !=e]
    print(l)
    l.extend([e]*cnt)
    return l

l=[1,1,2,3,4,5,1]
print(move_to_end(l,2))