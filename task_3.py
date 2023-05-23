import multiprocessing
from multiprocessing import Process
import time

count = 10

def task(n):
    while(n>0):
        time.sleep(1)
        n -= 1
if __name__ == '__main__':

    start = time.time()

    p1 = multiprocessing.Process(target=task, args=(count//2, ))
    p2 = multiprocessing.Process(target=task, args=(count//2, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print("Dastur ishlash vaqti: ", end - start)