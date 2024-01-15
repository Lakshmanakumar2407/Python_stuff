# Trying logging and timing....
from functools import wraps

def logger_decorator(some_func):
    import logging, os, datetime, pytz
    os.chdir('Python/Python_Basics')
    logging.basicConfig(filename='37.2_logging_created_for_decorator', level=logging.INFO)
    
    @wraps(some_func) # why decorator with arguments ??? check in ch 38..
    def wrapper_function(*args, **kwargs):
        logging.info('{} ran with arguments {} and key word argumnets {} at {}'.format(some_func.__name__, args, kwargs, datetime.datetime.now(tz= pytz.timezone('Asia/Kolkata'))))
        return some_func(*args,**kwargs)
    return wrapper_function

def time_calculator_decorator(some_func):
    import time

    @wraps(some_func)
    def wrapper_function(*arg, **kwargs):
        t1 = time.time()
        time.sleep(2) # delays execution for 2 seconds
        result = some_func(*arg, **kwargs)
        t2 = time.time() - t1
        print('The {} ran in {} seconds'.format(some_func.__name__, t2))
        return result
    return wrapper_function


'''
Be careful when stacking multiple decorators....
as you can see in the output instead of add wrapper_function is used in both log and console.... try running the code in your brain it makes sense
bascially the below decorators can be simplified as....
time_calculator_decorator(logger_decorator(add))
so when logger_decorator(add) is executed, it return wrapper_function (which executes add() within it) without executing it...
This wrapper_function, gets passed onto time_calculator_decorator as time_calculator_decorator(wrapper_function)
Hence we get the result as 'wrapper_function runs in x sceonds'

to avoid that we are passing the wrapper function in another decorator
'''

@time_calculator_decorator
@logger_decorator
def add(*args):
    result = 0
    for val in args:
        result += val
    return result

print(add(3,4))  

'''
Normally this would be tedious to include it in every function but now, It can be used on every function that is created
This is so cool!!!1
'''