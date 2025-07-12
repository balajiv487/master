import time

def print_number():
    for i in range(5):
        time.sleep(5)
        print(f"Print numbers :{i}")
def print_letter():
    for i in "ABCDE":
        time.sleep(5)
        print(f"Print letters :{i}")

print("Single process")
start_time=time.time()
print("start time :",start_time)
print_number()
print_letter()
print("Time taken single process: ", time.time()-start_time)