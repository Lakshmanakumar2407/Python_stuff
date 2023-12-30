# Break, Continue an pass

# BREAK
# printing only username in email
email = input('Enter you email-ID: ')
username = ''
for letter in email:
  if (letter == '@'):
    break
  username = username + letter
  
print(username)

# CONTINUE
# print email along with whats after the @
email = input('Enter you email-ID: ')
username = ''
for letter in email:
  if (letter == '@'):
    continue
  username = username + letter
  
print(username)

# PASS
# its is just a place holder not used instead of continue mostly used where we don't know what to code and we can't leave that place empty since it will cause error

email = input('Enter you email-ID: ')
username = ''
for letter in email:
  if (letter == '@'):
    pass
  username = username + letter
  
print(username)
