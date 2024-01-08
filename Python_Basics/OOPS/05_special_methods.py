# falling back to Employee class example...

class Employee:

    def __init__(self, first, last, pay):
        self.firstname  = first
        self.lastname = last
        self.pay = int(pay)
    
    def fullname(self):
        return self.firstname + ' ' + self.lastname
    
    def email(self):
        return str(self.firstname).lower() + '.' + str(self.lastname).lower() + '@company.com'
    
    def __repr__(self): 
        # repr dunder method is used as an UNAMBIGUOUS REPRESNTATION and meant to be read by developer
        return "Employee('{}', '{}', {})".format(self.firstname,self.lastname, self.pay)
    
    def __str__(self):
        # str dunder/ magic method is used with the intetniton of end user in mind
        # repr special method is used in cinjuction with str method as a way to fallback
        return '{} -> {}'.format(self.fullname(), self.email())


emp_1 = Employee('Jane', 'Trough', 500000)
emp_2 = Employee('Mary', 'Sue', 100000)
print(emp_1.email())

print(emp_1) # output be lke <_main__.Employee object at 0x0000234342f23
# print (emp_1) for better understanding should print out employee details or atributes as fall back
# to avoid thi special method __repr__ and __str__ is used

# after only using repr function in class the output will be like..
# Employee('Jane','Trough',500000)

# after using str method the output will be like
# Jane Trough -> jane.trough@company.com

'''
Even int as a special methods such as __add__, __sub__, __mul__ etc...
and even string method len() is a special method __len__
'''

print(2+1)
print(int.__add__(2,1))
print(len('testing'))
print('testing'.__len__())
print(str.__len__('testing'))

# CHECK DOCUMENTATION FOR MORE