# STRINGS

# STRING SLICING
s = 'strings in python are difficult for me'
print(len(s))
# command used to print length of the string
# in string the first letter is always assigned as 0
print(s[0])
print(s[0:10])
# here 10 indicates the count of characters to print from index 0 so it prints the characters upto 9th index
print(len(s[0:10]))
print('\n')

a = '2407200015'
s1 = a[0]
s2 = a[3]
print(s1+s2)
# Computer stores value in its own way unless until specified
# here computer stores its value as string unless it is explicitly mentioned by userthat it's an integ=er
print('\n')
s1 = int(a[0])
s2 = int(a[3])
print(s1+s2)
print('\n')

# STRING REPLECATION
s = 'trees are good for the environment'
print(s*3)
print(s[0:5]*5)
print('\n')

# STRING COMPARISION
x = 'India'
print(x=='India')
print(x=='india')
print('\n')

# another important example
print('apple'>'grapes')
# here the python compares the first letter of the string apple i.e 'a' to first letter of the string grapes i.e 'g'
# 'a' is obvious not greater than 'g' in alpahbetical order hence false
print('four'<'ten')
# if the strings are same...
print('abcde'<'abcde')
print('abcdef'<'abcde')
# in the above case its false because f can't be less than anything
print('\n')

# STRING INDEXING s[-1]
s = 'Python'
c = len(s)
print(c)
print(s[c-1])
print(s[c-2])
print(s[c-3])
print(s[c-4])
print(s[c-5])
print(s[c-c])
print('\n')
#or
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])
print('\n')

# In - like verifying if a string is in another string
print('a' in 'Ramayana')
print('b' in 'Ramayana')