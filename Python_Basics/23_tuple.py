# TUPLES (IMPORTANT)
import random

lt = list(range(random.randrange(1,100)))
# new found , the above list of varying range

l1 = [0,1,2,3,4,5,6,7,8,9] # can be initialized like this
l2 = list(range(10)) # can also be initialized like this

print(l1,l2,'\n')

#the definig representation of tuples visually is that they are represented using 'SMALL BRACES' unlike LISTS - SQUARE BRACES, SETS - CURLY (or) FLOWER BRACES

t1 = (1,2,3,4,5,6,7,8,9,10)
t2 = tuple(range(1,11))

print(t1,t2)

# another defining feature is that tuple cannot be changed, like adding, removing, replacing none of it can be done. where are list can be

# tuple can only be indexed and counted

'''t2[9] = 11''' # will throw error - tuple' object does not support item assignment

print(t2.index(10))
print(t2.count(7))

# these are only two methods available for tuples

# Where can tuples be used then??

# consider this example....

import string
alpha = string.ascii_letters
#print(alpha,type(alpha),'\n')

# making the alpha a tuple so that it can't be changed
tup = tuple(alpha)
#print(tup,type(tup))

# get a string from user
text = input('Enter your text here: ')
#text = text.replace(' ','')
#print(text)

# remove all values in string which isn't alphabets using the above tuple
for x in text:
  if (x in tup):
    continue
  else:
    text = text.replace(x,'')

print(text)
# in the above code the string is checked against the immutable (unchangeable) tuple to remove any characters other than alphabets

# tuple can be used as reference to check against

# the above can also e done without using tuple or we can convert string to list and use list methods to remove also

'''
another main advantage of tuple over list is 

size of tuple < size of list

since tuple won't be changed the python allocates less memory for the tuple unlike list
'''