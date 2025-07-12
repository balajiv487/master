import timeit

# Example: Timing a list comprehension
execution_time = timeit.timeit('[x*x for x in range(1000)]', number=1000)
print(f"Time taken: {execution_time:.6f} seconds")
