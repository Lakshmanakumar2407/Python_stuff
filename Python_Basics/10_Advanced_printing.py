# Advanced Printing (or) formatted printing

for n in range(5):
  print(n)
# in the above for loop every n is printed in the next line
# that is because, print() has default end characted of '\n'
# that can be changed by explicitly mentioning it

for a in range(5):
  print(a, end=' % ')
  print('\n')
# the sperating character can be anything

# Printing the date using variable
d = 24
m = 7
y = 2000
print('Your date of birth is:', end=' ')
print(d,m,y, sep='-')
# if the above program is done in same line then....
print('Your date of birth is: ',d,m,y,sep='-')
## as seen in the output an unwanted '-' is added

# another important thing to mention is that when the variable are seperated using commas, by default the seperator is value is ' '.

# that can be overrided by explicitly mentioning using the sep parameter

# FORMATTED PRINTING

print(f'{2} x {1} = {2}')
# here the variables are specified in the brackets
# as you can see this can reduce the complexity of using print statement

# another way to use is...
n = 2
m = 4
print('{0} x {1} = {2}'.format(n,m,n*m))

# other age old way to use is 
print('%d x %d = %d' %(n,m,n*m)) # I dont like this

# USING FORMAT SPECIFIER...
pi = 22/7
print(f'The value of pi is {pi}')
print('The value of pi is {0}'.format(pi))
print('The value of pi is %f' %pi)
print('/n')
# to limit the decimal to 3 digits
print(f'The value of pi is {pi:.3f}')
# no space mkae sure to remember it
print('The value of pi is {0:.3f}'.format(pi))
print('The value of pi is %.3f' %pi)

# we can also used digits to set the output length
print('{0:5d}'.format(11111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(111))
print('{0:5d}'.format(11))
print('{0:5d}'.format(1))