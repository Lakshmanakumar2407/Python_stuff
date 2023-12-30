import string

alphabets = string.ascii_lowercase

# MY WAY BEFORE WATCHING LECTURE
def cipher_text(t):
  n =''
  '''
  # LOOPING WAY
  for i in t:
    #print (i)
    n = n + caesar_cipher(i)
    #print(n)
  return n'''

  # RECURSIVE WAY
  if (len(t)==0):
    return ''
  n = caesar_cipher(t[0])
  #print(n)
  #print(t[1:])
  return n + cipher_text(t[1:])

def caesar_cipher(c):
  if c in alphabets:
    return (alphabets[alphabets.index(c)+1])
  if (c==' '):
    return c

# MY WAY AFTER GETTING IDEA FROM LECTURE

# create a dictionary and do it

text = input('Enter text to be ciphered: ')
text.lower()

dict = {}
for i in range(26):
  dict[alphabets[i]] = alphabets[(i+3)%26]
#print(dict)
a = ''
for x in text:
  a += dict[x]
print(a)

#print(caesar_cipher(text))
#print(cipher_text(text))