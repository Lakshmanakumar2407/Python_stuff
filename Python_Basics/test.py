import os
# os.chdir('Python/Python_Basics')
print(os.getcwd())
title_list = (os.listdir())
title_list_py = [title for title in title_list if title[-3:]=='.py' and title[0].isdigit() == True]
no_num = [title for title in title_list if title[-3:]=='.py' and not(title[0].isdigit() == True)]
for title in title_list_py:
    lits = title.split('_')
    if len(lits[0])<2:
        oldfilename = title
        newfilename = '0'+ oldfilename
        # os.rename(oldfilename, newfilename)
        print(newfilename)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)

for a,b in zipped:
    # print(a,b)
    pass

import datetime

# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

passed_tests = 0

for n in range(1, 13):
  score = - (n**2/1000) * (n**3 - 15*n**2 + 50*n) + 40
  if score == 40:
    passed_tests += 1

print([1,2]>[2,3])