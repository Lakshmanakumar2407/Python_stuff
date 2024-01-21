'''
Context managers in Python provide a convenient way to manage resources, 
such as file handling, network connections, or database connections, 
by ensuring that setup and teardown actions are performed properly. 
They are typically used with the with statement.

GPT definition
'''

# context manager using decorator concept
from contextlib import contextmanager
import os ,random

l = [random.randint(1,100) for _ in range(10)]

@contextmanager
def add(list1):
    
    print(f' the values to be executed are...{list1}')
    v = []
    for i in range(1, len(list1)):
        v.append(list1[i-1]+list1[i])
    # till here it's the setup block

    yield v
    # this pass a generator to the called function
    print(v)

    print('Inside teardown')
    list1.clear()
    # this performs the operation after the we exit the with block by back indenting

with add(l) as res:
    # here the add(l) yeild value v and it is assigned to res, with which we work on...
    print(res)
    res = res*2
    print(res)

add(l)
print(l)
# I think I get a gist of it... explanation above

print('\n\n')

# Lets try the above code usng classes
l = list(range(1,10,2))

class contxtmgr:
    def __init__(self,some_list):
        self.list1 = some_list
    
    def __enter__(self):
        print(f'Entering the __enter__ block, {len(self.list1)}')
        v = []
        for i in range(1, len(self.list1)):
            v.append(self.list1[i-1]+self.list1[i])
            if i+1 ==  len(self.list1): print(v)
        return v
    
    def __exit__(self,exe_type=None,exc_value=None,traceback=None):
        print('executed')
        print(v*2)

with contxtmgr(l) as res:
    c = []
    for v in res:
        c.append(v*2)
    print (c)

print()

# file handlingwith context managers....

class file_open:
    def __init__(self, path, mode,):
        self.dest = path
        self.mode = mode

    def __enter__(self):
        self.f = open(self.dest, self.mode)
        # for i in range(10): self.f.write(f'Test {i+1} \n')
        return self.f
    
    def __exit__(self,exe_type,exc_value,traceback):
        # self.f.write('exited \n')
        self.f.close()
        # print(self.f.closed)

os.chdir(r'Python\Python_Basics')
with file_open('31.2_test.txt', 'r+') as file:
    i = 0
    for line in file.readlines():
        if i>10:
            del line
        if i<=10: print(line, end='')
        i+=1

print()
print(file.closed + bool('twrf'), sep='-')
print()

# file opening and closing 
@contextmanager
def file_open_thru_func(filepath, mode):
    try:
        f = open(filepath,mode)
    except FileNotFoundError:
        print('File not found')
    else: 
        yield f
    finally:
        f.close()

with file_open_thru_func('31.2_test.txtnj','r') as flie:
    for line in flie.readlines():
        print(line, end='')

print()
print(flie.closed)
