l=[1,2,3,4]

import time
import threading
def calc_sq(l):
    for i in l:
        time.sleep(0.2)
        print(f"square of {i} is {i**2}")
t=time.time()
t1=threading.Thread(target=calc_sq,args=(l,))
t1.start()
t1.join()
print("done in:", time.time()-t)
