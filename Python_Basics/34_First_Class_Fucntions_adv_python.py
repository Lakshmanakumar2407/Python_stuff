"""
First Class Functions are those functions which

1. Can be assigned to a variable
2. Can be passed as arguments to a function
3. Functions can be returned from other functions

i.e treat functions as objects
"""

# Can be assigned to a variable

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

factorial_function = factorial # assigned to a variable
print(factorial_function(10))


# Can be passed as arguments to a function...
def square(n):
    return n**2

def apply_func(func, l):  
    return([func(n) for n in l])

square_value = apply_func(square,list(range(1,10)))
print(square_value) # square function passed as an argument to apply_function

print()

# Functions can be returned from other functions....
def logger(msg):

    def log_message():
        print(f'Hi {msg}')

    return log_message # returning function 

logging = logger('Amy')
print(logging) # logging doesn't store 'Hi Amy, It store the function log_message..
print(logging.__name__)
# now to run it...
logging()

print()

# so what's the use ???
# see if you can understand through this...
def html_tag(tag):

    def html_content(content):
        print(f'<{tag}>{content}</{tag}>')

    return html_content

html_creator = html_tag('p')
stuff1 = "Lorem ipsum"
stuff2 = 'Expelliarmus'
print(html_creator.__name__)
html_creator(stuff1)
html_creator(stuff2)