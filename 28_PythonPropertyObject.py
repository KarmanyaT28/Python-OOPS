# property(fget=None, fset=None, fdel=None, doc=None)


# fget − an instance method that retrieves value of an instance variable.

# fset − an instance method that assigns value to an instance variable.

# fdel − an instance method that removes an instance variable

# fdoc − Documentation string for the property.


# Let us define getter and setter methods without property methods

# A getter method retrieves the value of an instance variable, usually named as get_varname, 
# whereas the setter method assigns value to an instance variable − named as set_varname.

class Employee:
    'This is a base class for all the employees'

    def __init__(self,name,age):

        self.__name = name
        self.__age = age


    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self,name):
        self.__name=name
        return

    def set_age(self,age):
        self.__age=age
        return


e1=Employee("Karmanya",24)
print("Name: ",e1.get_name(), "Age: ",e1.get_age())


e1.set_name("Archana")
e1.set_age(45)

print("Name: ",e1.get_name(), "Age: ",e1.get_age())
