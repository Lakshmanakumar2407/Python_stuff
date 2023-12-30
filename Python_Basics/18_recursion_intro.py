# RECURSION (IMPORTANT)

# Let say we do sum of all numbers till a certain number...

def sum(n):
  sum = 0
  for i in range(n):
    sum = sum + (i+1)
  return sum

print(sum(98))

# or we can use the formula n*(n+1)/2

def sum2(n):
  sum = (n*(n+1))/2
  return sum

print(f'{sum2(98):.0f}')

# or there is more powerful computer way of doing it
'''
Lets say the sum of n numbers in given by f(n). then f(n) value can be interpreted as 

f(n) = f(n-1)+n

similary for factorial
f(n) = f(n-1)*n

similary for claculating compund interest
f(c) = f(c-1)*(1+r/100)

in the above function f(n-1), f(c-1) indicates the value of factorial or compound interest for number before the n

this is like callimg same function within same function. SUPERPOWERFUL IDEA

by using the above logic when we write code....
'''

def sumr(n):
  if (n == 1):
    return 1
  elif (n == 0):
    return 0
    sum = sumr(n-1)+n
  return sum

def fac(n):
  if (n == 1):
    return 1
  else:
    return fac(n-1)*n

def comp(n,r,y):
  if (y == 1):
    return n*(1+(r/100))
  else:
    return comp(n,r,y-1)*(1+(r/100))

print(sum(98))
print(fac(5))
print('{0:.2f}'.format(comp(200000,10,20)))