import timeit
def sum_function_to_test():
    sum = 0
    for i in range(20):
            sum += 1
    return sum

print(sum_function_to_test())
time_taken = timeit.timeit(sum_function_to_test, number=1000)
print("\n Total time taken: ", time_taken, "\n")
