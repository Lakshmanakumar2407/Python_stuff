# Function Practice

# python to code to calcute are and perimeter of rectange and circle
from math import *

def crap(shape,a_p):
  if (shape=='circle'):
    r = int(input('What is radius of circle? '))
    if (a_p=='area'):
      print(f'{pi*(r**2):.0f} sq. units')
    if (a_p=='perimeter'):
      print(f'{pi*r*2:.2f} units')
  if (shape=='rectangle'):
    l = int(input('Enter lenght: '))
    b = int(input('Enter breadth: '))
    if (a_p=='area'):
      print(f'{l*b:.2f} sq. units')
    if (a_p=='perimeter'):
      print(f'{2*(l+b):.2f} units')
    

shape = ''
while (shape!= 'exit'):
  shape = input('do you want to calculate for circle or rectange ? ')
  shape = shape.lower()
  if (shape!='exit'):
    a_p = input('what do you want to calculate for.. area or              perimeter? ').lower()
    crap(shape,a_p)
  else:
    pass

# though this code works this is not a correct use of functions.
# functions should be used calculate circle are and permiter seperatedf not like this one whole thing
'''A fuction should allow the code to be updated without making massive changes to the execution structure'''
    
# Write this code like a menu driven program