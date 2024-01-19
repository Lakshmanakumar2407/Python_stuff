print("Hello")
print("I'm from India")
# print('I'm from india''')
# the above code wont work because of quotation probelm

# print("We are We are "Rockers")
# wont work because of above error to
# in these kind of cases...

print('I\'m from india')
print("we are We are \"Rockers\"")
print("We are \t We are \n\"Rockers\"")

# for multiline printing
print('''Hello
how are you doing?
how is life?''')
# the '''  ''' camn be used for multiline commnetin too
'''hello this is
a test for that command
to prove it can be used for comments.
This won't be printed on the console'''

print("Hello",'cat')
n = input("Enter your cat name: ")
n = int(input('Enter age:'))
print('Hello Mr.',n, 'It seems your age is:',n)

# n is variable since its value changes

r = int(input('Plesse enter the radius value to calculate area of circle:'))
a = 3.14*r*r
print('area =',a)

# here 3.14 is litertal c ause it can't change (literally)

# variable is kind of basket that holds value according to specified type

# its always better to name variable according to use, like..
r = int(input("radius:"))
area_of_circle = 3.14*(r**2)
print(area_of_circle)

# TIPS FOR USING VARIABLE
#    Try making the variable self explanatory
#    Always write comments. either while writing the code or           when ater writing code. It helps other people and myself

# DYNAMIC TYPING - changeing value of variable while using
n = 10
print(type(n))
print(n)
n = n/3
print(type(n))
print(n)

# Multiple assignment
x, y = 1, 2
print(x,y)
x = y = z = 2
print(x,y,z)
x,y =1,3
x,y = y,x
print(x,y)

# Variable Deletion
x = 10
print(x)
del x # command to delete a variable
print(x)