# caesar cipher program

user_string = input('Enter the text to be ciphered: ')

alphabets = 'abcdefghijklmnopqrstuvwxyz'

output_string = ''

length = len(user_string)
# print(type(length),length)
#x = alphabets.index(user_string[0])+1
#print(type(x),x)
r_count = 2

for i in range(length):
  output_string += alphabets[(alphabets.index(user_string[i])+r_count)%26]
#print(alphabets.index(user_string[0]))
'''
replace_count = 26
output_string = alphabets[(alphabets.index(user_string[0])+replace_count)%26]
output_string = output_string + alphabets[(alphabets.index(user_string[1])+replace_count)%26]
output_string = output_string + alphabets[(alphabets.index(user_string[2])+replace_count)%26]
output_string = output_string + alphabets[(alphabets.index(user_string[3])+replace_count)%26]
# output_string = alphabets[output_string_index+1]
'''
print(output_string)