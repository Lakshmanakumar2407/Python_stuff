# NESTED FOR LOOP
## nEeD PrAcTiCe

# posibilities of 2 die

'''for i in range(6):
  print('\n')
  for j in range(6):
    print(i+1,j+1, sep='', end =' ')
print('\n')
print('These are the possibilities')
'''

# Find all prime numbers less than entered number

# Logic: Establish one loop for all the number below that number and another loop for checking if the number is divisbile by al the numbers below it

# Test code: 

#if (type(0.111) == type(0.2312)):
#  if (type(0.2342342) == type(0.234234)):
#    print('True')


'''
num = int(input("Enter the number: "))


snum = 1

if (num == 2):
  print('\x1B[3m'+'No output'+'\x1B[0m')
if (num == 1):
  print('\x1B[3m'+'No output'+'\x1B[0m')

snum = 1
tnum=1
while (snum<=num):
  snum1 = 6*tnum - 1
  snum2 = 6*tnum + 1
  if (snum2<=num and snum2%5!=0 and snum1%5!=0):
    print(snum1)
    print(snum2)
    snum = snum2
  tnum += 1
'''


# find the day wise total rainfall for the enetered duration of time e.g. week,month,etc...

days = int(input('Enter the total amount of dyas for which the rainfall is to be calculated: '))

# since we don't know the user input we will be using while loop

i=1
rainfall = 0
over_rainfall = 0
while(i<=days):
  print(f'you have entered day {i}')
  while(rainfall!=-1):
    rainfall = int(input('Enter todays rainfall:'))
    over_rainfall = over_rainfall+rainfall
  if (over_rainfall!=-1):  
    print(f'Todays rainfall is {over_rainfall}')
  else:
    print('0')
  over_rainfall = 0
  rainfall = 0
  i += 1
# can also be done using for loop check tutorial

# P4 find the length of the longest word from the set of words enetered by the user