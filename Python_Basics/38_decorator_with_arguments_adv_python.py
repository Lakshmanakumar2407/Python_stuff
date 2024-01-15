# so decorator with arguemnts is more like a decorator within a decorator...

def decorator_with_args_func(msg):
    def decorator_func(random_func):
        def wrapper_func(*args, **kwargs):
            print('{}, This was Printed before {} is executed'.format(msg, random_func.__name__))
            result = random_func(*args,**kwargs)
            print('{}, This was Printed after {} is executed'.format(msg, random_func.__name__))
            return result
        return wrapper_func
    return decorator_func


@decorator_with_args_func('Hi') # thats all, in the previous example...
def add(*args):
    res = 0
    for val in args:
        res += val
    return res

print(add(3,4,5))