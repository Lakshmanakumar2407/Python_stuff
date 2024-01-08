# using same class example...

class Employee:
    def __init__(self,first,last,company):
        self.firstname = first
        self.lastname = last
        self.company = company
        # self.email = '{}.{}@{}.com'.format(self.firstname,self.lastname,self.company)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname,self.lastname)
    
    @property
    def email(self):
        return '{}.{}@{}.com'.format(self.firstname,self.lastname,self.company)
    
    @fullname.setter
    def fullname(self, newname):
        first, last = newname.split(" ")
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        self.firstname = None
        self.lastname = None
        print("Deleted !")
    
    # def email(self):
    #     return '{}.{}@{}.com'.format(self.firstname,self.lastname,self.company)
        
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.firstname,self.lastname,self.company)
    
    def __str__(self):
        return "{} -> {}".format(self.fullname,self.email)
    
emp_1 = Employee('John','Smith','Python')
print('{} at {} with email id {}'.format(emp_1.fullname,emp_1.company,emp_1.email)) # any method which is converted as a decorator should be called like attribute i guess??

emp_1.firstname = 'Joe'
print('{} at {} with email id {}'.format(emp_1.fullname,emp_1.company,emp_1.email))
# We can see that the full name is update with new first name but email is not becase when the method fullname() is executed it calls self.firstname every time.
# one solution to solve this create a email method but in a deployed code introducing new email method will lead to changing all email attributes in the code to email method by adding '()'

# in this situtaion @ property can be used to ACCESS METHOD AS AN ATTRIBUTE
# by using it we cam see it workd, this is called getter i other languages it seems

emp_1.fullname = "Mary Sue"
print(emp_1.firstname) # the name didn't get changed to Mary. To do that we need to use setter. check class...
# beofre using setter on a method the method should be set to property
print(emp_1.fullname,emp_1.email)
print(emp_1)

# to use the deleter decorator...
del emp_1.fullname
print(emp_1.firstname)
print(emp_1)