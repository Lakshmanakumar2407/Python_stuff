# Function Practice

# pythin code using functions to calculate 1. upper case letters, 2.lower case letters, 3.total number of characters and 4.number of words

def upper_case(str):
  l = len(str)
  count = 0
  for i in range(l):
    #print(i)
    if (str[i].isupper()):
      count+=1
      pass
  return count

def lower_case(str):
  # l = len(str)
  count = 0
  for i in str:
    #print(i)
    if (i.islower() == True):
      count+=1
  return count

# Notice the different syntaxes used in above two similar functions

def charac(str):
  return len(str)

def words(str):
  count = 0
  for i in range(len(str)):
    if (str[i]==' '):
      #print(str[i-1])
      count+=1
      continue
  return count+1
    
text = input('Enter your text here: ')

print(f'Number of upper case charcater is: {upper_case(text)}')
print(f'Number of lower case charcters is: {lower_case(text)}')
print(f'Number of charcter in the above string is: {charac(text)}')
print(f'Number of words in the above string is: {words(text)}')