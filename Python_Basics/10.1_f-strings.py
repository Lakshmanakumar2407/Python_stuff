'''
F-Strings can be used in python from python 3.6

They are just more legible format of .format() method...
'''

import datetime as dt  
from math import * # brings math module entirely into the code so no need to specify math.pi but increases the memory

# instead of....
print('The value of {} to the power of {} is {}'.format(2,3,(2**3)))
print(f'The value of {3} to the power of {10} is {3**10}') # less words and even more readable

# some more examples...
print(f'{290} multipled by {4.23413} is {round(290*4.23413,3)}') # even methods can be used inside...
# alternate way to mento decimal is....
print(f'{290} multipled by {4.23413} is {290*4.23413 : .3f}')
print(f'The value of pi is {pi:.34f}')

print(f'The time now is {dt.datetime.now():%b %d %Y}')

l = []
for n in range(1,11):
    l.append(f'{n:03}') # padding numbers with 0's
print(l)