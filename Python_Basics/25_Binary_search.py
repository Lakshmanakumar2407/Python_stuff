# BINARY SEARCH

x = 1000
n = 0
while((x//10)!=0):
  x = x/2
  n+=1
#print(n)


# warm up binary search
#create a list and check if any random input given to the user is present or not
from random import *

def create_list(l,n):
  if (n==0):
    return l
  else:
    l.append(randint(1,1000))
    return create_list(l,n-1)

def sort_list(l):
  if (len(l)==0):
    return l
  else:
    m = min(l)
    l.remove(min(l))
    #print(m,l)
    return [m]+sort_list(l)

'''def no_of_times_to_iterate(l):
  print(l)
  count = 0
  ln = len(l); mid = ln//2
  #print(mid,type(mid),l[0:mid])
  #while (ln!=1):
  while(ln != 1):
    l1 = []
    l2 = []
    #print(ln!=1)
    l1 = l[:mid]
    l2 = l[mid:ln]
    print(l1,l2)
    ln = max(len(l1),len(l2))
    #print(ln)
    count +=1
'''

def binary_search_n(n,l):
  mid = len(l)//2
  while (len(l)!=0):
    #print(l[mid])
    if (l[mid]==n):
      return True
    if (l[mid]>n):
      l = l[:mid]
      #print(l)
      mid = len(l)//2
      if l[mid]==n:
        return True,l.index(n)
    elif (l[mid]<n):
      l = l[mid:]
      mid = len(l)//2
      if l[mid]==n:
        return True,l.index(n)
    if (n<l[0]) or (n>l[len(l)-1]):
      return False  

def binary_search_lecture(n,l):
  begin = 0
  end = len(l)-1
  while ((end-begin)>1):
    mid = (begin + end)//2
    if (l[mid]==n):
      return True, l.index(n)
    if (l[mid]>n):
      end = mid-1
    if (l[mid]<n):
      begin = mid+1
  if (l[begin]==n) or (l[end]==n):
    return True,l.index(n)
  else:
    return False

def binary_search_r_lecture_m(n,l):
  begin = 0
  end = len(l)-1
  mid = (begin+end)//2
  if (len(l)>1):
    if (l[mid]==n) or (l[begin]==0) or (l[end]==0):
      return True,l.index(n)
    if (l[mid]>n):
      return binary_search_r_lecture_m(n,l[:(mid-1)])
    if (l[mid]<n):
      return binary_search_r_lecture_m(n,l[(mid-1):])
  else:
    return False

def binary_search_r(n,l):
  if (n<l[0]) or (n>l[len(l)-1]):
    return False
  else:
    mid = int(len(l)/2)
    #print(mid,l[mid],l,'\n')
    if (l[mid]==n or l[0]==n or l[-1]==n):
      return True, l.index(n)
      #print(l[mid-1])
    elif (l[mid]<n):
      return binary_search_r(n,l[mid:])
    elif (l[mid]>n):
      return binary_search_r(n,l[:mid])
    else:
      return False


import time
# used to calculate the time to execute both binary search and obvious search...

length = 10000000

#list1 = create_list([],length)
#print(list1)
'''
@@@ IMPORTANT @@@

Recursion limit is set by most computers at 999 beyond that it wont work
it can be overriden by using sys tools -> need to study on that
'''
#list1 = sort_list(list1)
#print(list1)

user_number = int(input(f'Enter a random number between 1 to {length}:'))
l = [1,2,3,4,5,6,7,8,9,10]
# print(l[:5])


# THE ABOVE CODE EMPLOYS BINARY SEARCH

# the usual way to do it is obvious search..
def obvious_search(n,l):
  for a in range(len(l)):
    #print(a)
    if (a==n):
      return True, l.index(n)
  return False

a1 = time.time()
print(binary_search_r(user_number,list(range(length))))
a2 = time.time()

e1 = time.time()
print(binary_search_r_lecture_m(user_number,list(range(length))))
e2 = time.time()

c1 = time.time()
print(binary_search_n(user_number,list(range(length))))
c2 = time.time()

d1 = time.time()
print(binary_search_lecture(user_number,list(range(length))))
d2 = time.time()

b1 = time.time()
print(obvious_search(user_number,list(range(length))))
b2 = time.time()

print(f'time for binary search recursive is {a2-a1}')
print(f'time for recursive binary search lecture myway is {e2-e1}')
print(f'time for normal binary search is {c2-c1}')
print(f'time for normal binary search lecture way is {d2-d1}')
print(f'time for obvious search is {b2-b1}')