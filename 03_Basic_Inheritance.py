#!/usr/bin/python
# Define parent class

class Parent:
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(self):
        print ("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute : ", Parent.parentAttr)


# Define child class
class Child(Parent):
    def __init__(self):
        print ("Calling child constructor")

    def childMethod(self):
        print ("Calling child method")


# instance of child
c = Child()
# child calls its method
c.childMethod()
# calls parent's method
c.parentMethod()
# again call parent's method
c.setAttr(200)
# again call parent's method
c.getAttr()



# class A:        # define your class A
# .....

# class B:         # define your class B
# .....

# class C(A, B):   # subclass of A and B
# .....


# You can use issubclass() or isinstance() functions to check a relationships of two classes and instances.

# The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.

# The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class