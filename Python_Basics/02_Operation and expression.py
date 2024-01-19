# CONCATENATION
a = 78
b = 98
print(a+b)

a = 'samsung'
b = 'dex'
print(a+b)

a = 78
b = 98
print(a*b)

a = 'samsung'
b = 'dex'
# print(a*b)

# a*b doesn't work beacuse the program was not desiged to do it, '+' works because program was designed such way for the use of convinience

# works on list data types too!!
a = [3,4,5,'list']
b = [3.0,'is','awesome']
print(a+b)

a = [3,2,4]
b = [4,5,6]
print(a+b)
# doesn't do matrix like addition

# OPERATOR PRECEDENCE
a = 2+4*9/6-9
print(a)
# basic one () > left to right > *,\ >+,-

# TYPES OF OPERATORS

# ARITHMETIC OPERATORS (+,*,-,/,//,%,**)
print(8+3)
print(8*3)
print(8-3,3-8)
print(8/3)
print(8//3,'floor division - converts float -> int')
print(8%3,'modulus - gives remainder')
print(8**3,'power')
print('\n')

# RELATIONAL OPERATORS (>,<,>=,<=,==,!=)
print(6>5)
print(6<5)
print(5<5)
print(5<=5)
print(5>=5)
print(5==5)
print(5!=5)
print('\n')

# LOGICAL OPERATORS (and,or,not)
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('\n')
# both value should be 'True' to return 'True'

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('\n')
# atleast one value should be 'True' to return 'True'

print(not (True))
print(not False)
print('\n')
# it just inverts the value


# SHORT HAND OPERATOR
#    used make the typing code easier
a = 1
a = a+1
print(a)
print('\n')
# the above line a = a+1 can laso be return as...
a = 1
a += 1
print (a)
# this shorthand operation can be used with other functions too..
b = 83
b **= 3
print(b)

# CHAINING OPERATORS
x = 5
print(1<x<10)
# here it hsould not understood as the x should be between 1 and 10
# it should be interpreted as 1<x and x<10
# i.e True

print(10<x<20)
# 10<x and x<20 which is false

print(x<10<x*10<100)
# x<10; x<x*10; x<100 all true

print(10>x<=9)
# 10>x ; x<=9 ; both are true

print(5 == x>4)
# 5==x; x>4; both are ture
