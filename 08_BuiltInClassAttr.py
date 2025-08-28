
# Built-In Class Attributes in Python
# Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other attribute −

# SNo.	Attributes & Description
# 1	__dict__
# Dictionary containing the class's namespace.

# 2	__doc__
# Class documentation string or none, if undefined.

# 3	__name__
# Class name

# 4	__module__
# Module name in which the class is defined. This attribute is "__main__" in interactive mode.

# 5	__bases__
# A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

class Employee:
    'Base class for all employees'
    empCount = 0


    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

        Employee.empCount +=1


    def displayCount(self):
        print("Total Employees : %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name,"Salary: ", self.salary)

    

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
        




class Employee:
    def __init__(self, name="karmanya", age=24):
        self.name=name
        self.age=age

    def displayEmployee(self):
        print("Name : ", self.name, " age: ", self.age)



print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)