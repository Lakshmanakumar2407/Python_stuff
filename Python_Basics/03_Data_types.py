n = 5
print(n)
# n is an integer variable

r = 3.14
print(r)
# r is a float variable

l = 'laks'
print(l)
# l is a string variable

# displaying types of data types
print('n is an',type(n))
print('r is an',type(r))
print('l is an',type(l))

# New data type boolean
b1 = True # True - T Capital
b2 = False # False - F capital

print(b1, type(b1), b2, type(b2))

# convergence - converting 1 data type to another
# int to float
n = float(66578)
a = n
print(a,type(a))

# int to string
n = str(int(2342))
a = n
print(a,type(a))

# float to int 
# Only takes integer value does not round off the value
n = int(878.242)
a = n
print(a,type(a))

# float to string
n = str(34.29)
a = n
print(a,type(a))

# string to int & float
n1 = int('10')
n2 = float('23')
# n3 = float('ghu')
# doeesn't work
print(n1, type(n1), n2, type(n2))

# boolean conversion
b1 = bool(19)
b2 = bool(0)
b3 = bool(-19)
b4 = bool(8.0)
b5 = bool(0.0)
b6 = bool('strinhg')
b7 = bool('0')
b8 = bool('')
print(b1,b2,b3,b4,b5,b6,b7,b8)