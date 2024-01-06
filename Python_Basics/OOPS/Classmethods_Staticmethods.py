# getting to other example of my own inspired from internet

# lets use a class student which has the attributes name, overall_marks_in_subs,

from faker import Faker
from random import randint
import copy
import sys

# Set a new recursion limit (replace 5000 with your desired limit)
sys.setrecursionlimit(10000)
fake = Faker()

sort_iter = 0

class Student:

    # CLASS VARIABLE
    total_marks = 500 # declaring it as class variavle because it won't change and is constant for very student
    overall_students = 1000

    def __init__(self,name,marks):
        self.student_name = name
        self.marks = int(marks)

    def student_grade(self): # this is a regular method where the instance itself passes itself has the first argument
        self.percent = (self.marks/Student.total_marks)*100
        return round(self.percent,2)
    
    # CLASS METHOD
    # It is genrally used when we want to define a method that is bound to the class and not its instance
    # In the above method, the attribute percent is specific to each student based on their marks, a class method can't be used. 

    # lets create a useless class method total marks of students
    # to initiate a class method
    @classmethod
    def combined_maximum_marks_of_all_students(cls):
        return cls.total_marks*cls.overall_students # here cls can used in place of the class name Student
    
    # Some other common use cases of class methods...
    '''
    1. Alternative Constructors - Creating class methods to provide alterntive ways to create instance of classes. This example
    is used below

    2. Working with class variables - Accessing or modifying class variables within the method. This example is used above.

    3. Factory methods - Creating instances of the class within the class itself.

    '''

    # Lets say, If we get the data in the string method like "Name - marks", then we need to parse the string and seperate them into two entities and then call Student class and pass them as arguments
    # This might be repetive, so the use case of alternative constructors
    # the input to create a individual student instance is in the form "Name - Marks"
    @classmethod
    def from_string(cls,input_str): # like self,cls is an instance of class itself
        name, marks = input_str.split('-')
        # print(name,marks)
        return cls(name,marks) #if cls is not used in the function body, there is no need for classmethod
    
    # STATIC METHOD
    # a method is static when no instance of class or class itself is passed on as a argument
    # static method is method which just as logical connection to a class so included inside the class that's all
    @staticmethod
    def is_within_range(marks):
        # simple function that return if the mark is within 500, though there is no need for this function
        if marks < 500: # if I used Student.totalmarks instead of 500, t wouldn't be a static method
            return True
        else:
            return False


def highest_marks(dict):

    percent_list = []

    for i in range(Student.overall_students):
        percent_list.append(dict['student_'+str(i+1)][2])
    
    # test - 1 print(percent_list)

    # Sorting from highst to lowest
    percent_list_sorted = sorting(percent_list)

    # test - 2 print(percent_list_sorted)
    for i in range(Student.overall_students):
        if percent_list_sorted[0] == dict['student_'+str(i+1)][2]:
            student_name = dict['student_'+str(i+1)][0]

    return percent_list_sorted[0], student_name


def sorting(list1):
    # though there are other methods to do sort, I choose recursion

    global sort_iter # don't use operators on declaration itself
    sort_iter += 1
    # print(sort_iter)
    temp_list = copy.copy(list1)

    '''
    IMPORTANT LESSON LEARNED
    when copying list1 to temp_list only the reference value of list1 is passed to temp list
    and not the values of list itself. This is "call by reference". Eventhough i learned it, It's first time I made mistake in this, now can be understod better.
    '''

    # test 1 - print(list1,temp_list)

    for i in range(1, len(list1)):
        if list1[i] > list1[i-1]:
            # the below code can be shortened like this....
            #temp = list1[i]
            #list1[i] = list1[i-1]
            #list1[i-1] = temp
            list1[i],list1[i-1] = list1[i-1],list1[i]


    #test -2 print(list1,temp_list) # - helped me find reference by value error
    
    sum = 0
    for i in range(len(list1)):
        if temp_list[i] == list1[i]:
            sum += 1
            #pass

    if sum==len(list1):
        return list1
    else:    
        return (sorting(list1))

# check
##stu_1 = Student("Yolanda Robinson",'467')
##stu_1.student_grade()

Student.combined_maximum_marks_of_all_students() # Works

# creating list with string of student name and marks sperated by ' - '
input_list = []

for i in range(Student.overall_students):
    input_list.append(fake.name()+' - '+ str(randint(200,500)))
# print(input_list)

processed_dict = {}

for i in range(Student.overall_students):
    temp_holder = Student.from_string(input_list[i])
    processed_dict['student_'+str(i+1)] = temp_holder.student_name, temp_holder.marks, temp_holder.student_grade()
    
print(highest_marks(processed_dict))
print(sort_iter)

# Well this program went on a tangent for a simple class method practice