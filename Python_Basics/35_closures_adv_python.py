'''
Closure is an inner function tat remembers and has access to variable
in the local scope in which it was created even after the outer function 
has finished executing...
'''

def store_msg(msg):
    def print_msg():
        print(f'{msg}') # here the msg is free variable
        '''
        the difference between free varibale and nonlocal varibale is that, 
        non-local variable is stated expilicity like nonlocal msg, unlike
        free variable which remembers the msg as the function print_msg is 
        created inside function store_msg....

        Still there is some confusion for me tho...
        '''
    return print_msg

message1 = store_msg('Hello') # this function return the inner function print_msg without executing. to execute it...
message1()
message2 = store_msg('Hi')
message2()

print()

# EXAMPLE - 1

def html_tag(tag):
    def wrap_text(content):
        print(f'<{tag}> {content} </{tag}>')
    return wrap_text

print_h = html_tag('h1')
print_h('Title 1')

print_p = html_tag('p')
print_p('Lorem ipsum')

print()

# Example 2
import logging
import os

os.chdir('Python\\Python_basics')
print(os.getcwd())
logging.basicConfig(filename = '35.1_created_for_closures_demo.log', level=logging.INFO)

def logger(func):
    def logger_msg(*args):
        logging.info(f'Running {func.__name__} on parameters {args}')
        print(func(*args))
    return logger_msg

def add(*args):
    n =0 
    for val in args:
        n += val
    return n

def multiply(*args):
    n = 1
    for val in args:
        n*=val
    return n

add_func = logger(add)
multiply_func = logger(multiply)

add_func(1,2,3,4,5)
multiply_func(24,345,12341,12,67)