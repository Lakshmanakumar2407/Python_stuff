x = "Python -- String methods"

# Capitalizing and lowerising the word
print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.swapcase())
print('\n')

# checking ones...

x = "python"
print(x.islower())
print(x.isupper())
print(x.istitle())
print('\n')

x = "123"
print(x.isdigit())
x = '123ab'
print(x.isdigit())
print('\n')

x = 'abc'
print(x.isalpha())
x = '123ab'
print(x.isalpha())
print('\n')

x = '123ab'
print(x.isalnum())
x = '123ab#$%%^&'
print(x.isalnum())
print('\n')

## Strip....

x = " ---Py--thon---"
print(x.strip('-'))
print(x.lstrip('-'))
print(x.rstrip('-'))
print('\n')

## starts and ends with...
x = 'Python'
print(x.startswith('p'))
print(x.startswith('P'))
print(x.endswith('n'))
print(x.endswith('R'))
print('\n')

## others..
x = 'Python String Methods'
print(x.count('t'))
print(x.count('a'))
print(x.index('s'))
print(x.index('S'))
print(x.replace('S','vb'))
print(x.replace('n','r r r'))