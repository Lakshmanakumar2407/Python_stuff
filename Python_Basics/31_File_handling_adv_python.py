# Previously according to my knowledge....

f = open(r'Python\Python_Basics\31.2_test.txt','r') 
'''
If file is within the same working directory then we can just mention the file name. if not we need to mention the entire path

'r' indicate the mode in which we opened the file
some of the modes are....

r - open file in READ mode
w - open file in WRITE mode (overwrites the exsisiting data)
a - APPEND mode
r+ - READ AND WRITE mode

'''
print(f.mode) # tell the mode of file
print(f.read())
f.close() # the drawback of using this method is this...  we need to close the method by mentioning explicity
# to overcome the above limitation...
print(f.closed) # return bool val
print()


with open('Python\\Python_Basics\\31.2_test.txt','r') as test_f: # using this (context manager) we don't need to explicitly mention close()
    # we will also have access to object test+f outside the with block but we cant read or write in it
    
    # print(test_f.read())
    # the read() function brings the entire file into program, whicj might lead to some issue in case of large files, other methods through which we can access files are...
    # print(test_f.readline()) # prints only first line
    # print(test_f.readlines()) # prints all lines in a list format with newline characted at end
    # using readline but with loop...
    
    # since we don't when the file will return empty string while loop is better used here
    # loop_f = test_f.readline()
    # # when read line is used again and again when the file ends after some time it will retunrm empty string so....
    # while len(loop_f)>0:
    #     print(loop_f, end ='')
    #     loop_f = test_f.readline()
    # print()

    # we can also shorten the entire only to certain characters.. by passing paramenter through read func()
    read_count = 5
    loop_f1 = test_f.read(read_count) # only read first 5 charcters
    print(loop_f1) # thus looping through it....

    while len(loop_f1)>0:
        print(loop_f1, end = '^') # '^' indicator....
        # test_f.seek(0) # will move the read poit again to satrting point
        loop_f1 = test_f.read(read_count)

print()

print(test_f.closed)
# print(test_f.read()) # will throw error

print()

# WRITING FILES...
with open(r'Python\Python_Basics\31.1_File_created_using_write_function', 'w') as new_file:
    # no file is present in that name, it wll create a new file automatically....
    # To write something into it
    new_file.write("Some Stuff")
    new_file.seek(0)
    new_file.write("Fake_Stuff")
    print(new_file.writable())
    # stuff = new_file.readline() # wont work because it's only in write mode.... check by opening the file
    # print(len(stuff))
    pass

print()

# copying stuff from one file to another...
with open(r'Python\Python_Basics\31.2_test.txt', 'r') as read_file:
    with open(r'Python\Python_Basics\31.1_File_created_using_write_function', 'w') as write_file:
        for every_line in read_file:
            print(f"this is the line that is going to be copied - {every_line}", end = '')
            write_file.write(every_line)
        write_file.write("\n\n Copying done!!!")