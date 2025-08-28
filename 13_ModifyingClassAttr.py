# Modifying Class Attributes
# To modify the value of a class attribute, we simply need to 
# assign a new value to it using the class name followed by dot notation and attribute name.


class Employee:
    empcount = 0

    def __init__(self, name, age):

        self.name=name
        self.age=age


        # modifying class attribute
        Employee.empcount +=1
        print ("Name:", self.name, ", Age: ", self.age)
        # accessing class attribute
        print ("Employee Count:", Employee.empcount)


e1 = Employee("Karmanya",24)
print()

e2=Employee("Aanyaa",20)
print()

e3 = Employee("New",34)


# Significance of Class Attributes
# The class attributes are important because of the following reasons −

# They are used to define those properties of a class that should 
# have the same value for every object of that class.
# Class attributes can be used to set default values for objects.
# This is also useful in creating singletons. They are objects that are 
# instantiated only once and used in different parts of the code.


        