import collections
import matplotlib.pyplot as plt
import numpy as np
import string

data = "To be, or not to be, that is the question."
data=data.upper()
print(data)
data="".join(filter(lambda x:x in string.ascii_uppercase,data))
print(data)
counter=collections.Counter(data)
print(counter)
letter,count=zip(*counter.items())
print(letter,count)
indices=np.arange(len(letter))
print(indices)
plt.bar(indices,count,color='skyblue')
plt.xticks(indices,letter)
plt.xlabel("Letters")
plt.ylabel("Frequency")
plt.title('Frequency of Letters in the Given String')
plt.show()