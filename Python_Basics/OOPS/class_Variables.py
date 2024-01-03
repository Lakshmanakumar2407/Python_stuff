class Employee:
  
  pay_raise_percent = 4 # CLASS VARIABLE

  def __init__(self,fname,lname,salary):
    self.firstname = fname
    self.lastname = lname
    self.salary = salary
    self.name = fname + " " + lname

  def email(self): # this function belongs to class so it is called method
    return self.firstname + "." + self.lastname +"@company.com"
  
  def payraise(self):
    return self.salary*(1+(self.pay_raise_percent/100))
    # just using pay raise ampount won't make the program work we need to use either self or classname
    # Here it is better to use self because in some case, we nee to alter the pay for certain high ranking employee ...
    # It can be changed for that instance alone


emp_1 = Employee("John","Doe",5000)
# here class <Employee> got it's instance as emp_1
# i.e. emp_1 is an instance of class Employee
emp_2 = Employee("Jane","trough",2000)

# Class Variable

# Why class variable?
# It is used when there is no need for a feature to be different for variance instance where the class got inherited
# Here, the class employee don't need to have.... lets say attribute pay_raise_percent as different of every employee
# So a class variable can be used in this instance.... Check in the class
print(Employee.email(emp_1))
# both perform the same, but in the below code we need to explicitly state that
# the class employee's method email() is called for the instance emp_1

print(emp_1.payraise())