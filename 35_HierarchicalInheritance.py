# This type of inheritance contains multiple derived classes that are inherited 
# from a single base class. This is similar to the hierarchy within an organization.


class Manager:
    def ManagerMethod(self):
        print("I am the Manager")


class Employee1(Manager):
    def Employee1Method(self):
        print("I am Employee one")


class Employee2(Manager):
    def Employee2Method(self):
        print("I am Employee two")


emp1 = Employee1()
emp2 = Employee2()

# Employee 1 inheriting methods from Manager and Employee1
emp1.ManagerMethod()
emp1.Employee1Method()

# Employee 2 inheriting methods from Manager and Employee2
emp2.ManagerMethod()
emp2.Employee2Method()


