# The properties or variables defined inside a class are called as Attributes.
# An attribute provides information about the type of data a class contains.
# There are two types of attributes in Python namely instance attribute and class attribute.


# The instance attribute is defined within the constructor of a Python class and 
# is unique to each instance of the class. 
# And, a class attribute is declared and initialized outside the constructor of the class.


# Class Attributes (Variables)
# Class attributes are those variables that belong to a class and whose value is shared 
# among all the instances of that class. A class attribute remains the same for every 
# instance of the class.

# Class attributes are defined in the class but outside any method. 
# They cannot be initialized inside __init__() constructor. 
# They can be accessed by the name of the class in addition to the object. 
# In other words, a class attribute is available to the class as well as its object.


# Accessing Class Attributes
# The object name followed by dot notation (.) is used to access class attributes.


class Employee:
    name="Karmanya Tyagi"
    age= 24


# Instance of a class

emp = Employee()

# accessing class attributes

print("Name of the employee: ", emp.name)
print("Age of the employee: ", emp.age)






