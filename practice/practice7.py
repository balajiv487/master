import collections
from collections import Counter

def repeated_char(s):
    count=collections.Counter(s)
    d={}
    d={i:c for i,c in count.items() if c>1}
    return dict(sorted(d.items()))

s='dsfhehiuqgnmvka adbfdalghakjdhadshfa'
print(repeated_char(s))