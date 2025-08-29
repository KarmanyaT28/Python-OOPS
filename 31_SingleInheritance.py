# Python - Single Inheritance
# This is the simplest form of inheritance where a child class inherits attributes and methods from only one parent class.


# Parent Class
class Parent:
    def parentMethod(self):
        print("Calling Parent Method")


# Child Class
class Child(Parent):
    def childMethod(self):
        print("Calling Child Method")

# instance of Child Class
c = Child()
# Calling method of child class
c.childMethod()
# Calling method of parent class
c.parentMethod()