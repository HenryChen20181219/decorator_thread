'''目标函数带不固定参数的装饰器'''
import time

def decorator(func):
    def wrap(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        runtime = time.time()-start
        print(runtime)
    return wrap

@decorator
def do_something():
    for i in range(10000000):
        pass
    print('play game')

@decorator
def do_something2(user,name):
    for i in range(10000000):
        pass
    print(user+' play game '+name)

do_something()
do_something2('wangxiao','sanguosha')