# 1. SCOPE OF VARIABLE...

def func(x):
  x = x*2
  print(f'The value of x is {x}')

x = 5
print(f'The value of x is {x}')
func(x)
print(f'the value of x is {x}')
print('\n')
# By logic the last print function should print 10

# this is because call by value an dscope of varibale

'''
CALL BY VALUE
when we call the function func and input arguement x the x doesn't get passed... instaed only the value of x is gets passed. 
in other words..
the x inside the function func() is different from x in the outside program..

this concept is called scope of variable

here the x inside function func() is called LOCAL VARIABLE. the variable x is local to the function func()
the x outside the func() in the program is called GLOBAL VARIABLE
'''

# Inorder to make sure that no new variable is created when the function gets called and the global variable x is used inside the function....

def fun1():
  global a
  a=a*2
  print('the value of a is {0}'.format(a))

a = 5
print('The value of a is', a)
fun1()
print(f'the value of a is {a}')

# Here, when we mentioned global 'a' the python understand that there is varaible named 'a' outside fun1

# 2. TYPES OF FUNCTIONS

'''
There are 4 types of functions

1. user-defined fuctions (ex. func(), fun1())
2. In-built function (ex. print(), len(), sort())
3. String methods (ex. islower(),isupper(),isalnum())
4. library functions(ex. [log(),sqrt()] - math library,rand() - random library,calendar() - calendar library)
'''