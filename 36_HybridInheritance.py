# Combination of two or more types of inheritance is called as Hybrid Inheritance. 
# For instance, it could be a mix of single and multiple inheritance.


# In this example, we have combined single and multiple inheritance to form a 
# hybrid inheritance of classes.



class CEO:
    def CeoMethod(self):
        print("I am the CEO of the company")


class Manager(CEO):
    def ManagerMethod(self):
        print("I am the Manager of the company")


class Employee1(Manager):
    def Employee1(self):
        print("I am Employee 1, inheriting properties from Manager")


class Employee2(Manager,CEO):
    def Employee2(self):
        print("I am Employee 2, inheriting properties from Manager & CEO")


m1 = Manager()
e1 = Employee1()
e2 = Employee2()


# m1.CeoMethod()
# m1.ManagerMethod()

# e1.CeoMethod()
# e1.ManagerMethod()


emp = Employee2()

# method calls
emp.ManagerMethod() 
emp.CeoMethod()
emp.Employee2()
