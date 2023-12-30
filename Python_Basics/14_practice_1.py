# Practice

# 1. Birthday Paradox
# Paradox in which if we ask birthdate and month of random set of people there will be poeple with sasme birth date and months
# the porbablity increases with increase in random set

from random import *

l = []
# Initializing a list

for i in range(10):
  l.append(randint(1,365))
  # randint function generates random number between the number         specified in the brackets along with the specified numbers

l.sort()
print(l)
print('\n')
# sorts the value in list in ascending order

# check if the numbers are repeated...
i=1
flag = 0
while (i<len(l)):
  # len(l) gives no of elements in list
  if (l[i-1]==l[i]):
    flag = 1
    print('It repeats at ', l[i], end = '\n')
    pass
  i +=1

if (flag == 0):
  print(f"It doesn't repeat")

print('\n')
print('\n')


# 2. Naive search

# seach for a numbe rin big list

# initialize a list
'''
l = []
# imported random in the above program

# we need to find if the user entered number is in the list unless they enter -1

flag = 0
# we are setting flag so as to check for something in the loop. Its self explanatory and standard practice in code
num=0
count = 0
while (num!=-1):
  
  for i in range(1000):
    l.append(randint(1,100))
  print(len(l))
  
  num = int(input('Enter the number to be found: '))
  
  for i in range(len(l)):
    if (num==l[i]):
      count += 1
      flag = 1
      pass
  
  if (flag==1):    
    print(count,end='\n')
    count = 0
  
  if (flag==0):
    print('Not found')

'''
# 3. Sorting

# sorting the elements in list without using sort function :0
l = []

for i in range(100):
  l.append(randint(1,200))
print(l)
#print('\n')
temp = 0

for j in range(1,len(l)):
  for i in range(1,len(l)):
    if (l[i-1]>l[i]):
      temp = l[i-1]
      l[i-1] = l[i]
      l[i] = temp
      
#print(l)
print('\n')
print('\n')

# sorting done in tutorial is removing the smallest element from list and appendig it to new list and continue is on and on
# trying that...
l = []
m = []

for i in range(100):
  l.append(randint(1,200))

while (len(l)>0):
  min = l[0]
  
  for i in range(len(l)):
    if (l[i-1]<min):
      min = l[i-1]
  #print(l)
  l.remove(min)
  m.append(min)
print(m)

print('\n')

# 4. DOT PRODUCT of Vector matrix

m1 = [1,2,3,4,5]
m2 = [6,7,8,9,10]
sum = 0
if (len(m1)==len(m2)):
  for i in range(len(m1)):
    sum = sum + (m1[i]*m2[i])
  print(sum)
else: 
  print("Not a valid matrix")