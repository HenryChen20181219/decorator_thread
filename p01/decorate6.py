'''让装饰器带参数'''
import time

def decorator(max):
    def _decorator(func):
        def wrap(*args,**kwargs):
            start = time.time()
            for i in range(max):
                func(*args,**kwargs)
            runtime = time.time()-start
            print(runtime)
        return wrap
    return _decorator

@decorator(2)
def do_something():
    for i in range(10000000):
        pass
    print('play game')

do_something()

#相当于do_somthing = decorator(2)(do_something)

