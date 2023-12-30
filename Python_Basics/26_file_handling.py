# File handling using opython

# simply put, instead of manually typing something like list or dict or tuple for n numbers, it is stored in some file of some format which can be imported into the code

# this can't be done in replit so dont bother executing

f = open('a1.txt','w')
# the above command opens a text file named a1 in the working directory (or) creates one if not available 
# it also assign the opened/created txt file to variable f in 'w' - WRITE mode
# there are other modes which are listed below
'''
1. r: open an existing file for a read operation.
2. w: open an existing file for a write operation. If the file already     contains some data then it will be overridden but if the file is not    present then it creates the file as well.
3. a:  open an existing file for append operation. It won’t override       existing data.
4. r+:  To read and write data into the file. The previous data in the     file will be overridden.
5. w+: To write and read data. It will override existing data.
6. a+: To append and read data from the file. It won’t override            existing data.
'''
# to write or add data
f.write('wefwefw')
f.write('w3fwerfw')
# the write command wont add the new string in the next line, so we need to mention separately
f.write('\n')
f.write('wefwef')
# to cloase the file
f.close()
# to read the file
f = open('a1.txt','r')
s = f.read()
print(s)
f.readline()
# the above method reads each line in the file
# when excuted again it will read the next line and so on...