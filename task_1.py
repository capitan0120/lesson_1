import time
count = 10
def task(n):
    while(n>0):
        time.sleep(1)
        n -= 1

start = time.time()
task(count)
end = time.time()
print("Dastur ishlash vaqti: ", end - start)