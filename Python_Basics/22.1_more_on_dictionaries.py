# MORE ON DICTIONARIES

d = {}
# can be intialized like this
d = {'key':'value'}
# every dictionary should be in a standard form i.e. KEY-VALUE pair

# key is immuatbale and unique ; values can be repeated thuough
# thus key data type should be something which is immutable and hasble (check tuples). so no list (immutable) and tuple is yes and no. yes if hasable no if not hashable
# Value can be of any data type, lists tuples etc

d = {2:[2,4,6,8,10],3:[3,6,9,12,15],4:[4,8,12,16,20]}
for x in d:
  print(x, end = ' \t ')
  print(d[x],'\n')

# DICTIONARY METHODS
print(d.keys()) # generates 'list' of key alone
print(d.values()) # generates 'list' of all values
print(d.items()) # generates a 'list' of 'tuples' of key value pair which can hashable or non hashable based on the value datatype
print(d[2][3])

# All list metods can be used on dictionariy