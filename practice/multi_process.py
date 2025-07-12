import multiprocessing
import time
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"print_numbers : {i}")

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(f"print_letters: {letter}")

process1=multiprocessing.Process(target=print_numbers)
#process2=multiprocessing.Process(target=print_letters)

start_time=time.time()
print("start time :",start_time)
process1.start()
#process2.start()

process1.join()
#process2.join()

process1.terminate()


print("Time taken with multiprocessing: ", time.time()-start_time)
