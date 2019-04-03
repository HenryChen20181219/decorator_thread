'''被装饰过的函数的函数名'''
import time
import functools

def decorator(func):
    @functools.wraps(func)
    def wrap(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        runtime = time.time()-start
        print(runtime)
    # wrap.__name__ = func.__name__
    return wrap

@decorator
def do_something():
    for i in range(10000000):
        pass
    print('play game')


print(do_something.__name__)
