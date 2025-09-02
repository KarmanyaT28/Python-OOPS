# Abstraction is one of the important principles of object-oriented programming. 
# It refers to a programming approach by which only the relevant data about an object 
# is exposed, hiding all the other details. This approach helps in reducing the 
# complexity and increasing the efficiency of application development.


# Types of Python Abstraction
# There are two types of abstraction. 
# One is data abstraction, wherein the original data entity is hidden via a data structure
# that can internally work through the hidden data entities. 
# Another type is called process abstraction. It refers to hiding the underlying implementation 
# details of a process.



# Python Abstract Class
# In object-oriented programming terminology, a class is said to be an abstract class 
# if it cannot be instantiated, that is you cannot have an object of an abstract class. 
# You can however use it as a base or parent class for constructing other classes.

# Create an Abstract Class
# To create an abstract class in Python, it must inherit the ABC class that is defined 
# in the ABC module. This module is available in Python's standard library. 
# Moreover, the class must have at least one abstract method. 
# Again, an abstract method is the one which cannot be called but can be overridden. 
# You need to decorate it with @abstractmethod decorator.



from abc import ABC, abstractmethod

class demo(ABC):
    @abstractmethod
    def method1(self):
        print("Abstract Method")
        return
    def method2(self):
        print("Concrete method")

        
# obj = demo() # TypeError: Can't instantiate abstract class demo without an implementation for abstract method 'method1'



# The demo class here may be used as parent for another class. 
# However, the child class must override the abstract method in parent class. 
# If not, Python throws this error

# TypeError: Can't instantiate abstract class concrete class with abstract method


