# Instance Attributes


# As stated earlier, an instance attribute in Python is a variable that is 
# specific to an individual object of a class. It is defined inside the __init__() method.

# The first parameter of this method is self and using 
# this parameter the instance attributes are defined.


class Student():

    def __init__(self, name, grade):
        self.name=name
        self.grade=grade


        print("Name of student: ", self.name, " Grade of the student: ", self.grade)


# Creating instances

s1 = Student("Karmanya",'A')

s2 = Student("Shivam",'B')