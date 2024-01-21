'''
Yet to understand Duck typing so no notes on that...
'''

# EAFP - Easier to ask forgiveness rathen than permission...
list1 = [i for i in range(5)]

if len(list1)>=6:
    print(list1[5])
else:
    print('No index')

# EAFP
try:
    print(list1[5])
except IndexError:
    print('No index EAFP')

# it's just using try block more
    
dict_dum = {'name':'amy','age':29,'exp':4}
# dict_dum = {'name':'amy','age':29}

if 'name' in dict_dum and 'age' in dict_dum and 'exp' in dict_dum:
    print(f'{dict_dum["name"]} is of {dict_dum['age']} with {dict_dum['exp']} years of expereince')
else:
    print('Missing some Key')

# eAFp
try:
    print(f'{dict_dum["name"]} is of {dict_dum['age']} with {dict_dum['exp']} years of expereince')
except KeyError:
    print('EAFP-Missing sme keys')