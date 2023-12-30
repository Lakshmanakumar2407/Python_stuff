# IMPORTING LIBRARIES :)

import math
# here we are explicitly stating python to import math so that it can used while coding, without bring the math library into the code 
print(round(math.pow(2,23)))
# here math.pow indicates the program to use pow function from the math library
print(math.factorial(10))

# there are other libraries too...
# some libraries are used below to demonstarte other capabilitie of import function....

import random
print(random.random())
# print random number between 0 and 1
# it can be cumbersome to write to random. every time so to shorten it

import random as r
print(r.randrange(1,4))
# here r is used instead of random i.e. random is imported in the name of r
# randrange is funtion to produce random variable between 1 and 3 (not 4)

from calendar import *
# here the code explicitly states that python to import every function in calendar library into the code (i.e. bring it into the code)
print(month(2021,12))
# here as everything is imported there is no need to use calendar.month.... we can direlt use month if we want to use caldenar.month we can also shorten it like below

import calendar as c
print(c.calendar(1921))