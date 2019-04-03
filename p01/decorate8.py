'''装饰器类'''
import time

class Decorator(object):
    def __init__(self,max):
        self.max = max
        self.count = 0

    def __call__(self, func):
        self.func =func
        return self.call_func

    def call_func(self,*args,**kwargs):
        self.count += 1
        if(self.count==self.max):
            print('%s run more than %d times'%(self.func.__name__,self.count))
        elif(self.count<self.max):
            self.func(*args,**kwargs)
        else:
            pass

@Decorator(10)
def do_something():
    print('play game')

@Decorator(15)
def do_something1(name):
    print(name+' play game')

for i in range(20):
    do_something()
    do_something1('xiaobai')

