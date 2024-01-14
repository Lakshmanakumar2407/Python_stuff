# Generators are awesome!!!
import memory_profiler
from faker import Faker
import random as r
import time
# import matplotlib.pyplot as plt
fake = Faker()

########################################

name_list = [fake.name() for _ in range(100)]
gpa_list = [n for n in range(1,11)]

memory_at_start = memory_profiler.memory_usage()
print(memory_at_start)

def names_and_gpa_listway(number):
    for i in range(number):
        dummy_dict = {
            'id': i,
            'names': r.choice(name_list),
            'gpa': r.choice(gpa_list)
        }
    return dummy_dict

def names_and_gpa_generator(number):
    for i in range(number):
        dummy_dict = {
            'id': i,
            'names': r.choices(name_list),
            'gpa': r.choice(gpa_list)
        }
        yield dummy_dict    


act_n =1000 # play with this value

print()
time_return = []
time_generator = []
x_val = []

for n in range(1,act_n, 1000):# change the step size accordingly
    x_val.append(n)
    t1 = time.time()
    # print('generatornway')
    names_and_gpa_generator(n)
    t2 = time.time()
    # print('took {} seconds'.format(t2-t1))
    time_generator.append(t2-t1)
    # print('Memory used : {}'.format(memory_profiler.memory_usage()))


    t3 = time.time()
    # print('returnway')
    names_and_gpa_listway(n)
    t4 = time.time()
    # print('took {} seconds'.format(t2-t1))
    time_return.append(t4-t3)
    # print('Memory used : {}'.format(memory_profiler.memory_usage()))

# plt.plot(x_val,time_generator, label = 'Generator')
# plt.plot(x_val,time_return, label = 'list')
# plt.legend()
# plt.show()

'''
From the plot it can be seen that generators takes literally no memory

This is because, It doesn't execute. only when asked they start giving values one by one
still I didn't see the difference, so I will try the below example..
'''

print()
########################################

def mul_list(list1):
    result = []
    for val in list1:
        result.append(val*2)
    return result

def mul_gen(list1):
    for val in list1:
        yield val*2

dummy_list = [r.randint(1,100) for _ in range(100000)] # change this value to see effects

# testing for normal list way...
tlist_start = time.time()
dummy_list_store = mul_list(dummy_list)
list_op = [val*3 for val in dummy_list_store]
tlist_end = time.time()

# testing for generator way...
tgen_start = time.time()
dummy_gen_store = mul_gen(dummy_list)
gen_op = [val*3 for val in dummy_gen_store]
tgen_end = time.time()

print(f'Time for list = {tlist_end - tlist_start}')
print(f'Time for generator = {tgen_end - tgen_start}')

# In list comprehension instead of square bracket if () is used then it becomes generator

gen_ex = (val for val in range(100))
print(gen_ex) # generates geneartor object
# to print...
print([x for x in gen_ex])
# print([next(gen_ex) for _ in gen_ex]) - prints only odd numbers.......
# or
print(next(gen_ex)) # this one shows error as generator function as finished executing... need to initalize it again...