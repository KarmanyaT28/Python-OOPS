# Types of Constructor in Python
# Python has two types of constructor −

# Default Constructor
# Parameterized Constructor

# Default Constructor in Python
# The Python constructor which does not accept any parameter other 
# than self is called as default constructor.



class Employee:
    'This is base class employee for all the objects'

    def __init__(self):
        self.name="Bhavna"
        self.age=24

e1=Employee()

print("Name of the employee: {}".format(e1.name))
print("Age of the employee: {}".format(e1.age))

