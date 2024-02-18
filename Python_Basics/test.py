import os, datetime, time
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

time_now = datetime.datetime.now()
time_after_1s = time_now + datetime.timedelta(seconds=1)

# print(max(time_now, time_after_1s), time_now, time_after_1s)
# st = time.time()
# print(datetime.datetime.fromtimestamp(st))
# time.sleep(10)
# et = time.time()
# print(et)
# print(et-st)

def error_handler(*args):
   pass

file_path = 'Python_Basics\\43.1_csv_names_sample.csv'

dict1 = {'a':{1:'', 2:''}, 'b':{}}

for key in dict1:
   print(key)
   for key1 in dict1[key]:
      print(key1)
      print(max(dict1[key].keys()))