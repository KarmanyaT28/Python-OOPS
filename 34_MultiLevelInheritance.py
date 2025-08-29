# In multilevel inheritance, a class is derived from another derived class. 
# There exists multiple layers of inheritance. 
# We can imagine it as a grandparent-parent-child relationship.


# parent class

class Universe:
    def UniverseMethod(self):
        print("I am the Universe Class")


class Earth(Universe):
    def EarthMethod(self):
        print("I am the Earth Class")


class India(Earth):
    def IndiaMethod(self):
        print("I am the India Class")


person= India()


person.UniverseMethod()
person.EarthMethod()
person.IndiaMethod()
