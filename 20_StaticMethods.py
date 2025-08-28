# How to Create Static Method in Python?
# There are two ways to create Python static methods −

# Using staticmethod() Function
# Using @staticmethod Decorator


class Employee:
    empCount=0

    def __init__(self, name, age):

        self.name=name
        self.age=age

        Employee.empCount +=1

    # creating staticmethod
    def showCount():
        print(Employee.empCount)
        return
    counter = staticmethod(showCount)



e1 = Employee("Bhavna",24)
e2 = Employee("Karmanya",24)
e3 = Employee("John",35)


e1.counter()
Employee.counter()
        