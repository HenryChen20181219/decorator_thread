'''装饰器的单例模式'''

def singleton(cls):
    _instance = {}
    def wrap(*args,**kwargs):
        if cls not in _instance:
            _instance.cls = cls(*args,**kwargs)
        return _instance.cls
    return wrap

#创建具有装饰器的类
@singleton
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __call__(self,func):
        self.func = func#用类的地址保存函数名
        ###
        return self.call_func

    def call_func(self, *args, **kwargs):
        return
