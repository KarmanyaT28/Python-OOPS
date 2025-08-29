# The Python access modifiers are used to restrict access to class members 
# (i.e., variables and methods) from outside the class. 
# There are three types of access modifiers namely public, protected, and private.


# Public members − A class member is said to be public if it can be accessed from anywhere in the program.

# Protected members − They are accessible from within the class as well as by classes derived from that class.

# Private members − They can be accessed from within the class only.


# methods are defined as public and instance variable are private. 
# This arrangement of private instance variables and public methods ensures 
# implementation of principle of encapsulation.


class Employee:
    'This is a common base template for all the employees'

    def __init__(self, name="Karmanya", age=24):
        self.name = name
        self.age = age



e1 = Employee()
e2 = Employee("Bhavna",45)


print("Name: {}".format(e1.name))
print("Age: {}".format(e1.age))

print("Name: {}".format(e2.name))
print("Age: {}".format(e2.age))
