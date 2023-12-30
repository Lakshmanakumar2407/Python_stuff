# MORE RECURSION

# if there is 0 in list then return true or else return false

def check(x):
  if (len(x)==0):
    print(False)
  if (x[0] == 0) :
    print(True)
  else:
    # xc.pop(0)
    print(x)
    return check(x[1:len(x)])

l = [11,12,16,2,3,4,1,0,7]
print(l[1:len(l)])
check(l)

# Sorting using recursion
def sort(l):
  if (len(l)==1):
    x.append(l[0])
    return x
  else:
    x.append(min(l))
    l.remove(min(l))
    #print(x)
    return sort(l)
  
list = [2,5,-1,5,7,3]
x=[]
print(sort(list),'\n')

# recursively creating a list
from random import *

def list_create(l,n):
  if (n==0):
    #print(l)
    return l
    
  else:
    #print (l)
    l.append(randint(1,100))
    return list_create(l,n-1)

l = list_create([],2) # max recursion in replet is 995
print(l,len(l),type(l))
'''
a = [34]+[8]+[]+[9]
print(type(a.append(3))) # return nonetype
print (a)
'''

# RECURSION IS AWESOME 
# simply put it elminates the need of looping inside functions