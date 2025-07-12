import timeit
hello = "hello"
world = "world"
python = "Python"
is_ = "is"
easy = "easy"

def using_join():
    data = [hello, world, python, is_, easy]
    string = " ".join(data)
    return string

def using_concat():
    string = hello + " " + world + " " + python + " " + is_ + " " + easy
    return string

print(using_join())
print(using_concat())

using_join_time = timeit.timeit(using_join, number=1000_000)
using_concat_time = timeit.timeit(using_concat, number=1000_000)

print("Time taken by join: ", using_join_time)
print("Time taken by concat : ", using_concat_time)