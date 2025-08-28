class Employee:
    'This is a base class for all the employees'

    def __init__(self,name,age):

        self.name=name
        self.age=age


e1=Employee("Bhavna",25)

e2=Employee("Bharat",34)

        
print("Name of employee 1: {}".format(e1.name))
print("Age of employee 1: {}".format(e1.age))


print("Name of employee 2: {}".format(e2.name))
print("Age of employee 2: {}".format(e2.age))



class Employee1:
   'Common base class for all employees'
   def __init__(self, name="Karmanya", age=24):
      self.name = name
      self.age = age

e1 = Employee1()
e2 = Employee1("Aanyaa", 21)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))