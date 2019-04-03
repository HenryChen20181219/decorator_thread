'''最简单的装饰器'''
import time


def decorator(func):
    def wrap():
        start = time.time()
        func()
        runtime = time.time()-start
        print(runtime)
    return wrap

@decorator
def do_something():
    for i in range(10000000):
        pass
    print('play game')

do_something()