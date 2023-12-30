# MORE ON SETS

s = {1,2,3,4,5,1,4}
'''
what is unique about set?
set is enclosed using flower braces like in dictionary
and the elements inside are mentioned like list or tuples

so what is unique about set?
* it has no duplicate values
* It is unordered, it is simply a collection of values
* set itself is mutable but every value inside set should be immutable and hashable
'''
print(s)
# print(s[0]) # will throw erro rsince its unordered

# SET METHODS
# Set is amathematical concept so every set operatipon performed via maths can be perfomed in python

s1 = {1,2,3,4,9,8,7}
s3 = {5,6,7,8,9,3,0}

print(s1.issubset(s3)) # is_superset

# union
r1 = s1 | s3 # -> union operator sybol
r2 = s1.union(s3)
print(r1,r2)
# can be used in both ways

# intersection 
r3 = s1 & s3
r4 = s1.intersection(s3)
print(r3,r4)

# difference
r5 = s1 -s3
r6 = s3.difference(s1)
print(r5,r6)