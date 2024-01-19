# FOR LOOP

## It is used when we know the range the given input or the number of times the input is given unlike while loop


# to add first n numbers

'''n = int(input())
an = 0

for i in range(n):
  an = an + (i+1)
  i += 1

print(an)

# for loop for multiplication tables

n = int(input("Enter the number to get multiplication table: "))
l = int(input("Till what number: "))
m = 1

for i in range(l):
  print(n,"x",m,"=",(n*m))
  m += 1
'''
## working in range...

### Print even number

for x in range(0,11,1):
  print(x)

print('\n')

# in the for loop in range it usually has 3 parameters
# the first parameter indicates from which INDEX the loop has to start from.
# the second parameter indicates the length 
# third parameter is called STEP parameter, by how many steps the first parameter should add or subtract

# program to print odd number
for x in range(1,11,2):
  print(x)
print('\n')

# program to print number in reverse order
for x in range(9,-2,-5):
  print(x)
print('\n')

# for loop use case in string
text = 'No Fap King'
for letter in text:
  print(letter)