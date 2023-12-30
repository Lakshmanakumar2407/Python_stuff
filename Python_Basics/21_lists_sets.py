# LISTS AND SETS
l = [1,2,3,4,5]
s = {1,2,3,4,5}

# thats the differenc between sets and list ;)

'''visually lists are mentioned using square brackets and lists are mentioned using flower brackets

moreover in a set a value can't be repeated. juts like in maths
'''
s = {1,2,3,4,5,5,4,3,2,1}
print(s)
# doesn't print repetitive values

# and also sets have larger storage value than list..,
import sys
print(sys.getsizeof(s))
print(sys.getsizeof(l))
# can be seen from the above result.

'''
sets can't be referenced unlike lists like we can acces elemnt in list by mentioning l[x] but in set it's not possible.

we can only check if the value is present or not but can be referenced or used in other parts of the program
'''
# print(s[0]) #will throuw error - TypeError: 'set' object is not subscriptable

''' one thing where set is far more powerful than list is when we are finding for a ceratin element in large data sets....'''

l = list(range(10000000))
print(1 in l)
#  will return True very fats
print(-1 in l)
# will be very slow since it cheks against all value
s = set(range(10000000))
print(-1 in s)
# will return very fast try for a really big numer like trillion or billion

# :) even replits memory got filled
