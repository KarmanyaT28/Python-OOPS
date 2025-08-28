class Employee:
    empCount=0

    def __init__(self,name,age):
        self.name=name
        self.age=age

        print("Name: ", self.name, "Age: ", self.age)
        Employee.empCount +=1


    @classmethod
    def showCount(cls):
        print(cls.empCount)

    @classmethod
    def newEmployee(cls,name,age):
        return cls(name,age)
    

e1= Employee("Bhavna",26)
e2 = Employee("Karmanya",24)
e3 = Employee("Arjun",43)

e4 = Employee.newEmployee("Aanyaa",20)


Employee.showCount()

