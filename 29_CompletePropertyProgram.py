class Employee:
    'This is a base class for all the employees'

    def __init__(self,name,age):

        self.__name=name
        self.__age=age


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
    
    name = property(get_name,set_name,"name")
    age = property(get_age,set_age,"age")


e1=Employee("Bhavna",45)
print("Name: {}".format(e1.name))
print("Age: {}".format(e1.age))

e1.name="Karmanya"
e1.age=24


print("Name: {}".format(e1.name))
print("Age: {}".format(e1.age))