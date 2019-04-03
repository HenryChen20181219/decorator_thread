'''不是装饰器的装饰器'''
import time


def decorator(func):
    start = time.time()
    func()
    runtime = time.time()-start
    print(runtime)

def do_something():
    for i in range(10000000):
        pass
    print('play game')

decorator(do_something)