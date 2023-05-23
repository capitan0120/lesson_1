import time
from threading import Thread

count = 10
def task(n):
    time.sleep(1)
    n -= 1

t1 = Thread(target=task, args=(count//2, ))
t2 = Thread(target=task, args=(count//2, ))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print("Dastur ishlash vaqti: ", end - start)