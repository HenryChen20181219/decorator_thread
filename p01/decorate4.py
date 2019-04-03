'''目标函数带固定参数的装饰器'''
import time

def decorator(func):
    def wrap(name):
        start = time.time()
        func(name)
        runtime = time.time()-start
        print(runtime)
    return wrap

@decorator
def do_somthing(name):
    for i in range(10000000):
        pass
    print('play game '+name)

do_somthing('sanguosha')