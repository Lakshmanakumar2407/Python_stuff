# FUCTIONS

# its like building a own command for using in the code
# helps make the code more organised and introduces

# function to add to variables
def add(a,b):
  c = a+b
  # print(c)
  return c

# function to subtract variable
def sub(a,b):
  c = a-b
  #print(c)
  return c

# funsction to find discounted value
def disc(cost,d):
  fcost = cost - (cost*(0.01*d))
  #print(fcost)
  return fcost

add(12313,42534)

fnum = 34532
snum = 3424
sub(fnum,snum)
# the variable can also used as parameters. Python equates the given variable to available variable in the function just be careful with the datatypes

disc(2314,20)

# this works just to print the output. it wont work if we need to work with the output value
# for example

#num = add(231,123123) + sub(12321,131)*disc(234214,3)
#print(num)

# will throw error because the function just prints. When we check the output value it shows
print(type(add(231,3)))

# It shows nonetype which means it odes nothing. to chang ethi swe need to return the value whoch can be done by... (refer the above funcyion)

# now after changing if we print
print(add(231,123123) + sub(12321,131)*disc(234214,3))

# VOILA

# Practicing previous exampole using functions

# finding minimum number in the list

def list_min(l):
  min = l[0] #should'nt use min because it's a built in command
  for i in range(len(l)):
    if (l[i]<min):
      min = l[i]
  return min

def list_max(l):
  max = l[0]
  for i in range(len(l)):
    if (l[i]>max):
      max = l[i]
  return max

def list_prefix(l1,z):
  return z+l1

l1 = [2,3,6,6,8,1]
z = [3,4,2,6,6]
n = list_prefix(l1,z)
print(n)
print(list_min(n))
print(list_max(n))

# Sorting using functions

def sort_list(l):
  x = []
  for i in range(len(l)):
    mini = l[0]
    for j in range(len(l)):
      if (l[j]<mini):
        mini = l[j]
    x.append(mini)
    l.remove(mini)
  return x,l

def my_sort(l):
  for j in range(len(l)):
    for i in range(1,len(l)):
      if l[i-1]>l[i]:
        temp = l[i-1]
        l[i-1] = l[i]
        l[i] = temp
  return l

# the above functions are complex...
# the main idea of the function is to break it into small parts so that the it can be easier to code and to be understood

# the above functions can be broken down as ...
# 1. find the minimum of the list
# 2. using the min from that functio in loop tp sortlike below..

def sort_list1(l):
  x =[]
  for i in range(len(l)):
    min = list_min(l)
    # calling another function within function :)
    x.append(min)
    l.remove(min)
  return x
  
print(sort_list1([45,223,1,11,123]))