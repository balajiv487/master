def alpha_numeric(s):
    print(s)
    final=[]
    cnt=1
    for i in range(1, len(s)):
        print(f"s[i] is :{s[i]}" )
        print(f"s[i-1] is :{s[i-1]}")
        if s[i]==s[i-1]:
            cnt +=1
        else:
            final.append(s[i-1]+str(cnt))
            cnt=1
    final.append(s[-1]+str(cnt))
    return final
s="aaaabbbccd"
print(alpha_numeric(s))
