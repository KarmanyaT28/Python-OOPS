# Python Self Parameter

'''

The self Parameter
The self parameter is a reference to the current instance of the class

It is used to access properties and methods that belong to the class
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello, my name is {}".format(self.name))



p1 = Person("John", 22)
p1.greeting()

