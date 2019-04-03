def decrator1(number):
    print(number)
    def decorator(func):
        print('123'+'xiaobai')#只要装饰了就会运行
        print(number)
        def wrap(name):
            #函数执行前
            print(name)
            print(number)
            for i in range(2):
                func(name)
        return wrap
    return decorator

@decrator1(3)
@decrator1(2)
def func1(name):
    print(name,123)

func1('xiaobai')