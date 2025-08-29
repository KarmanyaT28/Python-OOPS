# The Python method overriding refers to defining a method in a subclass with the 
# same name as a method in its superclass. In this case, the Python interpreter 
# determines which method to call at runtime based on the actual object being referred to.

# You can always override your parent class methods. One reason for overriding 
# parent's methods is that you may want special or different functionality in your subclass.


class Parent:
    def myMethod(self):
        print("Calling myMethod from Parent Class")


class child(Parent):
    def myMethod(self):
        print("Calling myMethod from Child Class")


c = child()

c.myMethod()


# Another Example


class Employee:
    def __init__(self,nm, sal):
        self.name=nm
        self.salary=sal
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary

class SalesOfficer(Employee):
    def __init__(self,nm, sal, inc):
        super().__init__(nm,sal)
        self.incnt=inc
    def getSalary(self):
        return self.salary+self.incnt

e1=Employee("Rajesh", 9000)
print ("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1=SalesOfficer('Kiran', 10000, 1000)
print ("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))






# __init__ ( self [,args...] )

# Constructor (with any optional arguments)

# Sample Call : obj = className(args)


# __del__( self )

# Destructor, deletes an object

# Sample Call : del obj


# __repr__( self )

# Evaluatable string representation

# Sample Call : repr(obj)


# __str__( self )

# Printable string representation

# Sample Call : str(obj)