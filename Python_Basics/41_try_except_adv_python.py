try:
    '''
    This block run the code in whihc we might expect error, like when an user signs into webpage and 
    their credentials are not available....
    '''
    open('Test.File','r')
except FileNotFoundError:
    '''
    If the user's credentials are not available, then instead of throwing an ugly error, this EXCEPT block, 
    will catch that error and say something like 'File doesnt exsist or something appropriate to the error
    '''
    print('OOps, File is not there')
else:
    '''
    If the there are user credentials then the code in ELSE bock will execute,
    like opeing the user account in case of this example
    '''
    print('Yeah File Opened')
finally:
    '''
    The code in FINALLY block will execute regardless of whether the TRY block will raise exception or not
    '''
    print('Executed')