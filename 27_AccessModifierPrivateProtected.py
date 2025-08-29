# To indicate that an instance variable is private, prefix it with double underscore (such as "__age").
# To imply that a certain instance variable is protected, prefix it with single underscore (such as "_salary").


class Employee:
    'This is a base class for employees'

    def __init__(self, name="Karmanya" , age=24 , salary=250000):
        self.name=name #public variable
        self.__age=age #private variable
        self._salary=salary #protected variable


    def displayEmployee(self):
        print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)



e1=Employee()
e2=Employee("Bhavna",45,100000)
e3=Employee("Arjun",29,3838383)

print("****************************")
print("Name: {}".format(e1.name))
# print("Age: {}".format(e1.__age))
print("Age: {}".format(e1._Employee__age)) # Name Mangling
print("Salary: {}".format(e1._salary))
# print("****************************")
# print("Name: {}".format(e2.name))
# print("Age: {}".format(e2.__age))
# print("Salary: {}".format(e2._salary))
# print("****************************")
# print("Name: {}".format(e3.name))
# print("Age: {}".format(e3.__age))
# print("Salary: {}".format(e3._salary))
# print("****************************")
