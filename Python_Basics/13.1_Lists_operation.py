# List Operations

# order or adding maters
l1 = [1,2,3]
l2 = [4,5,6]
l12 = l1+l2
l21 = l2+l1
print(f'{l12}\n{l21}') # use of normal printing makes indentation uneven because of commas

# to repeat a list woth fixed values n number od time
l1 = [0]*10
l2 = ['s','r','k']*5
print(f'{l1}\n{l2}\n')

# boolean operations on string
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]
print(f'{l1==l2}\n{l2==l3}\n')
l4 = []
l5 = [1]
l6 = [2,3]
print(f'{l4<l5}\n{l6<l3}\n{l5<l1}\n')
# list compares element wise

# MUTABLITY of LISTS (VERY IMPORTANT)

l = [1,2,3,5]
l[3] = 4
print(l,'\n')
# this seems non sensical but it is veru important 
# this can't be done in strings

s = 'Stringgs'
#s[5] = 'h'
# print(s) # throw errpor cause strings are immutable


# another example...

x = 5
y = x
x =10
print(x,y) # prints 10,5

# when we use strings see what happens
l1 = [5]
l2 = l1
l1[0] = 6

print(l1,l2,'\n') # though tthe output would be [6] [5]

'''
V.V.IMPORTANT

The above code works like that because in the integer case...
when we use y in the code, python creates seperate variable y (like a container) and puts the value of x in that..
in the case of strings...
the python doesnt create new list named l2, instead it give the list variable l1 another name l2 so it doesn't change
'''

# so how to create new list and check if its not just another name for already defined variable

l1 = [1,2,3]
l2 = l.copy() # method
l3 = list(l1) # defining
l4 = l1[:] # slicing

print(l2 is l1)
print(l3 is l1)
print(l4 is l1)
print(l5 is l1,'\n')

# Lists through function
def addint(x):
  x = x+1
  return x

def addlist(a):
  a.append(1)
  return a

x = 5
print(x)
print(addint(x))
print(x,'\n')
# in the addint case only x's value is passed not x itself. it is called CALL BY VALUE

y = [5]
print(y)
print(addlist(y))
print(y,'\n')
# in the addlist def whole y is passed not y's value. It is called CALL BY REFERENCE

# if the datatype is immutable then 'call by reference' is used in functions. other wise 'call by value


# LIST METHODS
l = [1,2,3]
print(l)
l.append(4) # adds an element with value 4
print(l)
l.remove(2) # removes an element with value 2
print(l)
# the above method unless specified explicitly,  will perfom theri operation on the parent list
x = l.copy() # copies, creates new list not like assigning another name
print(x)
x.insert(2,10) # inserts elemnent with value 10 at the index position 2 and does not replace or remove
print(x)

x.remove(3) # same like above
print(x)
x.pop(2) # remove any value at the index 2
print(x,'\n')

import random
# l = list(range(random.randint(1,100)))
l = [234,23,456345,3453456,686,677857,5234]
print(l,type(l))
l.sort() # sorts ascendingly
print(l.sort()) # string methods return nonetype
l.reverse() # reverses the list
print(l)