class Counter:
    def __init__(self,max_count):
        self.max_count = max_count
        self.current=0

    def __iter__(self):
        return self
    def __next__(self):
        if self.current>=self.max_count:
            raise StopIteration
        self.current +=1
        return self.current
counter=Counter(3)
for i in counter:
    print(i)