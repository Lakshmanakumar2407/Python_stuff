# DICTIONARIES (IMPORTANT)
'''
d = {}
# dictonry can  be crated like this

d['aravind'] = 98
d['balu'] = 23
d['chintu'] = 76
d['Draupath'] = 81
print(d)
print('\n')

# another way to use for loop in lists
l = [1,324,1234213,2342,12341233,2112435645,56758,0,6896,54674,46,46]
for i in l:
  print (i)
print('\n')

'''
l = ['it','was','the','you','where','where','what','how','it','who','what','whom','the','is','will','where','whom','can','can','might','will','who']

#print(l.index('where'))
#print(len(l))
#print(l)
#print('\n')

s = set(l)
#print(s)


# code to count the repeated word in the list

for i in l:
  print(i)

print('\n')

# Set is created
for x in l:
  print(x) # all repetive words removed

print('\n')

d = {}
# in this dictionaru set will be like book keeper...

for x in s:
  d[x]=0

#print(len(d))

#print(d)
print('\n')

# the fllowing code is ingenius
for x in l:
  d[x] = d[x] + 1

'''
in the above code, we are using l (list) instead of set to pass its value to index dictionary

since in set there are no repetitions and we assigned each element in the set to zero when we pass the list throguh d...

if the word gets repeated it will simple add 1 to it

for example lets say a word 'it' is in list and repated n number of times

we create a set for the list as it removes repettion

when we use for loop in list if 'it' get mentioned twice then the code will add the number of time the it appeared to dictionary conatining the unique value

''' 
# P.S. Small corecction in the above explanation, there is no need to create new set to make the words unique, juts directly input list to dictionary will automaticaly remove repetitions

#print(d)
print('\n')

# to find the dictionary element with larget repetition
maxi = 0
answord=''
for i in d:
  if (d[i] > maxi):
    maxi = d[i]
    answord = i

print(maxi,answord)

# PUT SIMPLY....
# dictionary is a datat type to hold certain values which are unique to each other nd these each unqiue value might contain one or more elements that may be repated in other unique valuue

# look at the example below...

from random import *

dict = {}
list_name = []
list_age = []
list_work_hours = []
min_wage = 10
list_wage = []

for i in range(10):
  list_name.append('person'+str(i+1))
  list_age.append(randrange(18,60))
  list_work_hours.append(randrange(0,12))
  list_wage.append(list_work_hours[i]*min_wage)

print(list_name,'\n',list_age,'\n',list_work_hours,'\n',list_wage)
print('\n','\n')

for i in range(len(list_name)):
  dict[list_name[i]] = [list_age[i],list_work_hours[i],list_wage[i]] 

print(dict)

# this above code is a perfect example of usage of dictionaries

# as seen in the above code each and every person should be unique or we should choose something unique to them

# the dict can also conatiner any type of dataset be it list, float,string, integer or even another dictionary

# to access a certain elemets value in dict...

print(dict['person8'][1])

# thats how it should be accessed