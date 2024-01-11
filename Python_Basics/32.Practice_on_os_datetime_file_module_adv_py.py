'''
TASK
1. Create a directory named 'Practice_directory' in the current directory - ✔
2. Create n file and write the creation date and file name into it - ✔
3. rename the file's in the format of renamed_'file_name' - ✔
4. delete all files and write the name of files in deleted_files.text - ✔

'''

import os
import datetime as dt
import pytz

original_working_directory = os.getcwd()

os.chdir(original_working_directory + r'\Python\Python_Basics')
current_working_directory = os.getcwd()
# print(current_working_directory)

if os.path.exists(os.getcwd() + r'\Practice_directory') == False:
    os.mkdir('Practice_directory')
# os.rmdir('Practice_directory')

os.chdir(current_working_directory + r'\Practice_directory')

Practice_directory = os.getcwd()

# creating 10 files of names file_1, file_2 ....

number_of_files_to_be_created = int(input("Enter the number fo files you wish to create : "))
# n = 1

def file_creation(n):
    india_tz = pytz.timezone("Asia/Kolkata")
    fmt = "%b %d, %Y - %H:%M UTC %z Hours "
    for i in range(n):
        # if os.path.exists(f'{Practice_directory}\\file_{i+1}.txt') == False:
        with open(f'{Practice_directory}\\file_{i+1}.txt','w') as file_created:
            file_creation_time = dt.datetime.now().astimezone(india_tz)
            file_created.write(f'This file was created on {file_creation_time.strftime(fmt)}')
    return None

# Removing files which were not within the range n...
# print(f'{Practice_directory}\\test.txt')

def unwanted_file_deletion():
    global number_of_files_to_be_created
    no_of_files = number_of_files_to_be_created
    while os.path.exists(f'{Practice_directory}\\file_{no_of_files+1}.txt') == True:
        os.remove(f'{Practice_directory}\\file_{no_of_files+1}.txt')
        no_of_files += 1
    return None


# file renaming
def file_renaming():
    global number_of_files_to_be_created
    n = number_of_files_to_be_created
    for i in range(n):
        old_file_path = '{0}\\file_{1}.txt'.format(os.getcwd(),i+1)
        new_file_path = '{0}\\file_{1}_renamed.txt'.format(os.getcwd(),i+1)
        os.rename(old_file_path,new_file_path)
    return None

# file deletion and logging to a file called deleted_files_txt
def logging_and_files_deletion():
    global number_of_files_to_be_created
    n = number_of_files_to_be_created
    with open('{}//deleted_files.txt'.format(Practice_directory), 'w') as f_log:
        for i in range(n):
            with open('{}//file_{}_renamed.txt'.format(Practice_directory, i+1), 'r') as f_read:
                f_log.write(os.path.basename('{0}\\file_{1}_renamed.txt\t'.format(os.getcwd(),i+1)))
                f_log.write('-\t{}\n'.format(f_read.readline()))
            if i==(n-1): print("Success")
            os.remove('{}\\file_{}_renamed.txt'.format(Practice_directory, i+1))
    return None

file_creation(number_of_files_to_be_created)
unwanted_file_deletion()
file_renaming()
logging_and_files_deletion()    