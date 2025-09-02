# Encapsulation is the process of bundling attributes and methods within a single unit. 
# It is one of the main pillars on which the object-oriented programming paradigm is based.

# We know that a class is a user-defined prototype for an object. 
# It defines a set of data members and methods, capable of processing the data.

# According to the principle of data encapsulation, the data members that 
# describe an object are hidden from the environment external to the class. 
# They can only be accessed through the methods within the same class. 
# Methods themselves on the other hand are accessible from outside class context. 
# Hence, object data is said to be encapsulated by the methods. 
# In this way, encapsulation prevents direct access to the object data.


# Implementing Encapsulation in Python
# Languages such as C++ and Java use access modifiers to restrict access to class members 
# (i.e., variables and methods). These languages have keywords public, protected, and 
# private to specify the type of access.

# A class member is said to be public if it can be accessed from anywhere in the program. 
# Private members are allowed to be accessed from within the class only. 
# Usually, methods are defined as public, and instance variables are private. 
# This arrangement of private instance variables and public methods ensures the 
# implementation of encapsulation.

# Unlike these languages, Python has no provision to specify the type of access 
# that a class member may have. By default, all the variables and methods in a Python 
# class are public, as demonstrated by the following example.

# Example 1
# Here, we have an Employee class with instance variables, name and age. 
# An object of this class has these two attributes. 
# They can be directly accessed from outside the class, because they are public.


class Student:
    def __init__(self, name="Karmanya", age=24):
        self.name=name
        self.age=age


s1 = Student()
s1.name="Aanyaa"
s1.age=20

print(s1.name)


# print ("Name: {} marks: {}".format(s1.name, s2.marks))
# print ("Name: {} marks: {}".format(s2.name, s2.marks))


# In the above example, the instance variables are initialized inside the class. 
# However, there is no restriction on accessing the value of instance variables 
# from outside the class, which is against the principle of encapsulation.

# Although there are no keywords to enforce visibility, 
# Python has a convention of naming the instance variables in a peculiar way. 
# In Python, prefixing name of a variable/method with a single or double 
# underscore to emulate the behavior of protected and private access modifiers.

# If a variable is prefixed by a single double underscore (such as "__age"), 
# the instance variable is private, similarly if a variable name is prefixed 
# with a single underscore (such as "_salary")



# Example 2
# Let us modify the Student class. Add another instance variable salary.
#  Make name private and marks as private by prefixing double underscores to them.


class Student:

   def __init__(self, name="Rajaram", marks=50):
      self.__name = name
      self.__marks = marks
   def studentdata(self):
      print ("Name: {} marks: {}".format(self.__name, self.__marks))
      
s1 = Student()
s2 = Student("Bharat", 25)

s1.studentdata()
s2.studentdata()
print ("Name: {} marks: {}".format(s1.__name, s2.__marks))
# print ("Name: {} marks: {}".format(s2.__name, __s2.marks))




# Name mangling is the process of changing name of a member with 
# double underscore to the form object._class__variable. If so required, 
# it can still be accessed from outside the class, but the practice should be refrained.

# In our example, the private instance variable "__name" is mangled by 
# changing it to the format

# obj._class__privatevar
# So, to access the value of "__marks" instance variable of "s1" object, 
# change it to "s1._Student__marks".

# Change the print() statement in the above program to −

# print (s1._Student__marks)
# It now prints 50, the marks of s1.

# Hence, we can conclude that Python doesn't implement encapsulation 
# exactly as per the theory of object-oriented programming. It adapts a more mature 
# approach towards it by prescribing a name convention and letting the programmer use name 
# mangling if it is really required to have access to private data in the public scope.

