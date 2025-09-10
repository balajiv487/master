words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count={}
for i in words:
    if i not in word_count:
        word_count[i]=1
    else:
        word_count[i]+=1

print(word_count)
#Helo