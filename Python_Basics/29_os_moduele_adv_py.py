import os

# DETAILS

print(os.getcwd()) # getced - get current working directory
os.chdir('/Users/laksh/Documents/Programming/Python/Python_Basics') # chdir change directory
print(os.getcwd())
list_of_files = os.listdir() # lists the files in directory
# print(len(list_of_files), list_of_files)
# mod_list = [file for file in list_of_files if file[0] == True]
# print(len(mod_list),"\t",mod_list)

# printing stats of the file
print()
print('Stats of file')
print(os.stat('26_file_handling.py'))
print(os.stat('26_file_handling.py').st_size)

print()
for dirpath,dirname,filename in os.walk('/Users/laksh/Documents/Programming/Python'):
    print('Directory path : {}'.format(dirpath))
    print('Directory names : {}'.format(dirname))
    print('File name is {}'.format(filename))
    print()

# CREATION

os.mkdir('test') # used to make single only single directory
os.rmdir('test') # removes only the mentioned directory and doesn't remove its contents. 
# before creating a new directory with same name the old directory shoould be deleted
os.makedirs('test1/test1.1') # used to make directories recursively, mkdir can't do it. so better to use makedirs everywhere
os.removedirs('test1/test1.1') # similar to makedirs but used to remove

# MODIFICATION
# renaming current file
# os.rename('/Users/laksh/Documents/Programming/Python/Python_Basics/29_os_moduele_adv_py.py','/Users/laksh/Documents/Programming/Python/Python_Basics/29_renametest_os_moduele_adv_py.py')
# renaming back to original
# os.rename('/Users/laksh/Documents/Programming/Python/Python_Basics/29_renametest_os_moduele_adv_py.py','/Users/laksh/Documents/Programming/Python/Python_Basics/29_os_moduele_adv_py.py')

# renaming sorting file to sorting and lambda
# os.rename('/Users/laksh/Documents/Programming/Python/Python_Basics/28_sorting_adv_python.py','/Users/laksh/Documents/Programming/Python/Python_Basics/28_sorting_and_lambda-func_adv_python.py')\
print()
print(os.environ) # print all the environments avalianle
# to select a specific environemnt
print(os.environ.get('USERPROFILE'))

print()
# lets create a imainiry directory
file_path = os.path.join(os.environ.get('USERPROFILE'),'/tmp/test.txt')
print(file_path)

# some other ways of verification and accessing
print(os.path.basename(os.getcwd()))
print(os.path.dirname(os.getcwd()))
print(os.path.exists(file_path))
print(os.path.exists(os.path.dirname(os.getcwd())))
print(os.path.split(os.getcwd()))
print(os.path.isdir(os.path.dirname(os.getcwd())))