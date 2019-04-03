#并发，并行
#线程
import threading
import time

def sing():
    print('有线程时')
    time.sleep(1)

# for i in range(5):
#     sing()

for i in range(5):
    t = threading.Thread(target=sing)
    t.start()