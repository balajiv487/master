def alpha_numeric(s):
    print(f"Alpha numeric string is: {s}")
    final=""
    for i in range(0,len(s),2):
        char=s[i]
        num=int(s[i+1])
        final += char*num
    return final
s='a4b3c2d1e0'
print(alpha_numeric(s))