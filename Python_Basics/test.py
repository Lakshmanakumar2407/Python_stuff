import os
os.chdir(r'Python\Python_Basics')
print(os.getcwd())
title_list = (os.listdir())
title_list_py = [title for title in title_list if title[-3:]=='.py' and title[0].isdigit() == True]
for title in title_list_py:
    lits = title.split('_')
    if len(lits[0])<2:
        oldfilename = title
        newfilename = '0'+ oldfilename
        os.rename(oldfilename, newfilename)