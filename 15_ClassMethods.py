# Methods belongs to an object of a class and used to perform specific operations. 
# We can divide Python methods in three different categories, which are 
# class method, instance method and static method.

# A Python class method is a method that is bound to the class and not to the instance of the class. 
# It can be called on the class itself, rather than on an instance of the class.

# Most of us often get class methods confused with static methods. 
# Always remember, while both are called on the class, static methods do not have access to 
# the "cls" parameter and therefore it cannot modify the class state.

# Unlike class method, the instance method can access the instance variables of the an object. 
# It can also access the class variable as it is common to all the objects.


# Creating Class Methods in Python
# There are two ways to create class methods in Python −
# Using classmethod() Function
# Using @classmethod Decorator


class Employee:
    empCount = 0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Employee.empCount +=1

    def showcount(self): # This is an instance method
        print(self.empCount)

    counter = classmethod(showcount) #This way converts the showcount method into class method 
                                     #and assigns it to the name counter
                                     #That means you can now call it on the class itself, not just an object


e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)

e1.showcount() # Calling instance method through object
Employee.counter() # Calling class method through class


