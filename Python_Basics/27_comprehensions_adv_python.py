# LIST COMPREHENSIONS

# generate a list with 2 times the values in list
list1 = [1,2,3,4,5,6,7,8,9,10]
newlist =[]

for val in list1:
    newlist.append(val*2)

print(newlist)

# the above code can be simplified into single one line program using comprehension
comprehended_newlist = [val*2 for val in list1]
# voila

print("\n\n")

# $print only even numbers and power them to cube$

newlist = []
comprehended_newlist = []

# using the beginner approach
for val in list1:
    if val%2==0:
        newlist.append(val*val*val)

#using list comprehension
comprehended_newlist = [val**3 for val in list1 if val%2 == 0]

# checking...
print(newlist)
print(comprehended_newlist) # same putput

print("\n\n")

# # nested for looping using list complrehensions
# # transposition of matrix

# # traditionally
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# t_matrix = []
# for i in range(3):
#     temp_mat = []
#     for j in range(3):
#         temp_mat.append(matrix[j][i])
#     t_matrix.append(temp_mat)

# comprehended_t_matrix = [matrix[j][i] in for i in matrix for j in i ]

# $Flattening of nested lists$
dummy_list = [[1,2,3],[4,5,6],[7,8,9]]
flattened_list = []
for i in range(len(dummy_list)):
    for j in range(len(dummy_list[i])):
        flattened_list.append(dummy_list[i][j])
print(flattened_list)

# list comprehension method
flattened_list = [num for sublist in dummy_list for num in sublist]
print(flattened_list)

print("\n\n")

# $print a letter nad num pair for each letter in 'abcd' and each number in '0123'$
abcd0123 = []
for letter in 'abcd':
    for num in '0123':
        abcd0123.append((letter,num))
print(abcd0123)

# List Comprehension
abcd0123 = [(letter,num) for letter in 'abcd' for num in '0123']
print(abcd0123)

print('\n\n')

# $ creating a set
import random as r
dummy_list = []
dummy_set = set()
for i in range(100):
    dummy_set.add(r.randint(1,5))
    dummy_list.append(r.randint(1,5))
print(dummy_set)

# List comprehension
dummy_set = {n for n in dummy_list}
print(dummy_set)

print('\n\n')

# $Dictonary Creation - Dictionary with name and number of words in them excluding ' '
from faker import Faker
fake = Faker()
name_list = []
for i in range(5):
    name_list.append(fake.name())
dummy_dict = {}
for name in name_list:
    dummy_dict[name] = len(name.replace(" ",""))
print(dummy_dict)

# list comprehension
dummy_dict = {name: len(name.replace(" ", "")) for name in name_list} 
print(dummy_dict)

print("\n\n")

# $filtering - print prime numbers in first 1000 numibers
prime_number = []

# code for generating prime numbers, ignore
# for i in range(1,100):
#     Flag = True
#     for j in range(2,i):
#         if i%j == 0:
#            Flag = False
#            #print(i,j)
#     if Flag == True:
#         prime_number.append(i) 

# generating list of numbers using list comprehension
l = [n+1 for n in range(0,100)]

# function for prime number check
def prime(n):
    if n <= 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
        
for num in l:
    if prime(num) == True:
        prime_number.append(num)
print(prime_number)

# using list comprehension
prime_number = [n for n in  range(1,100) if prime(n)==True]
even_odd_prime = ['even' if n%2 ==0 else 'odd' for n in prime_number]
print(prime_number)
print(even_odd_prime)