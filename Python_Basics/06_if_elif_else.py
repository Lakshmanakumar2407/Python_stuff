# If, Ifeles(elif), else

## check if the number is even or not

n = int(input('Enter the number: '))
if (n%2 == 0):
   print('Its an even number')
else :
  print('Its an odd number')


## grading of a student - nested if

marks = int(input("Enter the marks of the student: "))
m = marks
if (0<=m<=100):
  if (90<= m <= 100):
    print('A')
  if (80<= m <90):
    print('B')
  if (70<=m<80):
    print('C')
  if (60<=m<70):
    print('D')
  if (m < 60):
    print('F')
else:
  print('Invalid Input')

## grading of student - elif 

## In the baove example where multiple if statements are used, the program checks for every if condition before terminating

## in the case of elif, the program checks the first if condition if it fails it will check th elif condition where the conditions are alos shortened to reduce repetitiveness

## so in elif the program terminates when on eleif condition returns true.
marks = int(input("Enter the marks of the student: "))
m = marks
if (0<=m<=100):
  if (90<= m <= 100):
    print('A')
  elif (m < 90):
    print('B')
  elif (m<80):
    print('C')
  elif (m<70):
    print('D')
  elif (m < 60):
    print('F')
else:
  print('Invalid Input')