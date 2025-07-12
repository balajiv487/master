def double_char(s):
    print(f"s: {s}")
    str=""
    for i in s:
        str +=i*2
    return str
s="abc"
print(double_char(s))

l=[1,2,3,4,5,6]
a,*b,c=l
print("a:",a)
print("b:",b)
print("c:",c)

