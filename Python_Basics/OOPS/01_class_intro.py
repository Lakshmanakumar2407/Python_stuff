import sys

# Why Class?
# I think It enabales us to containerize or split up complext part of the problems into smaller tasks whch can be reused and solved simply

class Employee:
  def __init__(self,fname,lname,salary):
    self.firstname = fname
    self.lastname = lname
    self.salary = salary
    self.name = fname + " " + lname

  def email(self): # this function belongs to class so it is called method
    return self.firstname + "." + self.lastname +"@company.com"


emp_1 = Employee("John","Doe",5000)
# here class <Employee> got it's instance as emp_1
# i.e. emp_1 is an instance of class Employee
emp_2 = Employee("Jane","trough",2000)

# In the class employee, the data such as firstname, lastname, salary, name are known as attributes and the function __init__ (also knon as constructor) in other languages 

print(id(emp_1),"\t",id(emp_2))
print(type(emp_1),"\t",type(emp_2))
print(sys.getsizeof(emp_1),"\t",sys.getsizeof(emp_2))
print(sys.getsizeof(emp_1.firstname),"\t",sys.getsizeof(emp_2.firstname))

print(emp_1.firstname, emp_2.lastname)

print(emp_1.email(),"\t", emp_2.email())
# when emp_1.email is called it means to call the instance of class employee
# which is emp_1. This call usually gets converted by system as follows

# Class Variable
print(Employee.email(emp_1))
# both perform the same, but in the below code we need to explicitly state that
# the class employee's method email() is called for the istanc emp_1