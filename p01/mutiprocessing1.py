import multiprocessing
import time


def run_proc():
    while True:
        print('--22-----')
        time.sleep(2)

p = multiprocessing.Process(target=run_proc)
p.start()