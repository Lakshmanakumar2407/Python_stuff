# Decorators - well... they look tough, lets try to understand them....

def decorator_function(some_func): # First class Function principles
    def wrapper_function(*args, **kwargs):
        print()
        print('executed through decorator function....')
        return some_func(*args, **kwargs) # closures concept is applied here
    return wrapper_function # First class Function principles

def display():
    print('Hello Python')

output = decorator_function(display) # First class function principles
print(output.__name__)
output()
# well that's a decorator...

# what when some arguments is passed....

def add(a,b):
    return a+b

output = decorator_function(add)
# output(4,5)
# throw's error like this..
# TypeError: decorator_function.<locals>.wrapper_function() takes 0 positional arguments but 2 were given

# to avoid this... we add args and kwargs in wrapper func
print(output(2,4))

# so the initiator output = decorator_function(add) can be replaced by @decorator_function

@decorator_function
def mul(*args):
    result = 1
    for val in args:
        result *= val
    return result

print(mul(2,5,3,2,5,53,2,2))

# what's the use of decorator function????
'''
It helps us modularize tasks which might be used repeated inside a function... like logging and time recording
Let me try that in 37.1 ....
'''