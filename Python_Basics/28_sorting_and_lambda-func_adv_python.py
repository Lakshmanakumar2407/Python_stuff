import random as r

l = []
for i in range(r.randint(10,20)):
    l.append(r.randint(1,1000))

print(l)

# For general sorting l.sort() function can be used..
l.sort()
print(l)

print("\n")

# if we pass l.sort into prit function then it will return none
print(l.sort()) # None
s = l.sort()
print(s) # None

print("\n")

# and l.sort can't be assigned to other variabes too, which is not desirable 
# Enter SORTED function
s = sorted(l)
print (s)
# We can reverse the sorting order using the parameter reverse
s = sorted(l, reverse=True) # by default reverse is false
print(s)

print("\n")

# What if we want to sort the list after performing a operation of list

# Noob way - for sorting based on negative value of number
neg_l =[]

def mk_neg(n):
    return -1*n

for v in l:
    neg_l.append(mk_neg(v))
print(neg_l)
s_neg_l = sorted(neg_l)
print(s_neg_l)

# list comprehension way 

neg_l = [-n for n in l]
s_neg_l = sorted(neg_l)
print(s_neg_l)

# this can be made into one line using lambda functions and sorted function
s_neg_l = sorted(l, key = lambda n : -n)
print(s_neg_l)

print("\n")

# sorting class attributes
class person:
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def __repr__(self):
        return "Person ('{0.name}',{0.age})".format(self)

person1 = person('Jane',45)
person2 = person('Ellie',34)
person3 = person("Lily",23)
person4 = person('Amy',29)

person_list = [person1,person2,person3,person4]
sorted_person_list = sorted(person_list, key = lambda p: p.name) # passing without on what basis should it be sorted would throw error. so need to pass key
print(sorted_person_list)