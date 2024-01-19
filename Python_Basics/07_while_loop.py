# WHILE LOOP
# Code executes until the condition in while loop is satisfies
# code that goes on endlessly until it satisfies a certain condition

# suitable conndition to use when we don't know the limit of the condition or when the user will stop givng input

## Indepence...
'''
year = int(input('When did India get Independence?'))
count = 0

while (year!=1947):
  print('Please try again: ')
  year = int(input('When did India get Independence?'))
  count += 1
  
print('You got it right after',count,'times')
'''

## Factorial example

''' num = int(input('Enter the number fro which factorial needs to be calculated = '))
i = 1
k = num

while ((k-i)!=0):
  n = n*(k-i)
  print (k-i)
  i += 1

## the above doesn't work with 0

fact = 1 # making o=0 factorial as 1

while (num>0):
  fact *= num
  num -= 1

print(fact, num)


## find the number of digits in the given number
num = int(input("Enter the number: "))
num = abs(num)
count = 1
mul = 10
num_p = 1

while(num_p != num):
  num_p = num%mul
  mul *= 10
  count += 1
  print(mul, count)

# this can also be achieved using // operator
print(count-1)

print(0!=0)
# Reverse the digits in given number
numt = int(input())
num = abs(numt)
rnum = 0
tnum = num


while (tnum!=0):
  rnum = (rnum*10) + (tnum%10)
  tnum = tnum//10

if (numt>0):
  print(rnum)
elif(numt<0):
  print(-rnum)
'''

# Find if the number is palindrome
numt = int(input())
num = abs(numt)
rnum = 0
tnum = num


while (tnum!=0):
  rnum = (rnum*10) + (tnum%10)
  tnum = tnum//10

if (numt>0):
  if (rnum == numt):
    print('Palindrome')
  else:
    print('Not Palindrome')
if(numt<0):
  if (-rnum == numt):
    print('Palindrome')
  else:
    print('Not Palindrome')