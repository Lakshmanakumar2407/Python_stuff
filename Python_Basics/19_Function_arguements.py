# TYPES OF FUNCTION ARGUEMENTS

def add(a,b,c):
  return a+b-c

print(add(1,2,3))
print('\n')

'''
in the above code ...

def bloack - function definition
add (print-area) - function call
a,b,c - parameters
1,2,3 - arguments
return - will pass the value back to place where it was called

in the above example when we assign 1,2,3 is passed as arguments to function parameters it is assigned as 
a = 1; b = 2; c = 3

It all seems common sense... but what if the function is definded in this way
'''

def add1(c,a,b):
  return a+b-c

print(add1(1,2,3))
print('\n')

'''
The value gets changed. If it should not be changed, then we need to modify function

since the result changes based on position of the arguements they are called POSITIONAL ARGUEMENTS

to solve this kind of issue we need to use something called
KEYWORD ARGUEMENTS

It can be done using expicitly mentioned variable to values..
'''

def add2(a,c,b):
  return a+b-c

print(add2(a=1,b=2,c=3))
print('\n')

# We get the original value

# Another kind of issue faced when using funtions are we forget the no of parameters in the function

# This can be solved using something called DEFUALT ARGUEMENTS
# this can be implemented like...

def add3(a=23,b=121,c=13):
  return a+b-c

print(add3())
print(add3(1))
print(add3(1,2))
print(add3(a=1,b=2,c=3))
print('\n')

# It can be observed in the above function that if no argument is passed, then function gets executen based on the 'DEFAULT ARGUEMENTS' that are defined beforehand when the function definition is written

'''
Thus there are 3 types of function

1. Positional Arguements
2. Keyword Arguements
3. Default Arguements

'''

# RETURN...

def add4(a,b,c):
  print(a+b-c)

print(type(add4(1,2,3)),add4(1,2,3))

# Since the function doesn't return any value it is assigned as NoneType.. 