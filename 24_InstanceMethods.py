# The getattr(obj, name[, default]) − to access the attribute of object.

# The hasattr(obj,name) − to check if an attribute exists or not.

# The setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

# The delattr(obj, name) − to delete an attribute.


# A method with self as one of the formal arguments is called instance method, as it is called by a specific object.

class Employee:
   def __init__(self, name="Bhavana", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

e1 = Employee()
e2 = Employee("Bharat", 25)

e1.displayEmployee()
e2.displayEmployee()


# Add a 'salary' attribute
e1.salary = 7000 
# Modify 'name' attribute
e1.name = 'xyz' 
e1.displayEmployee()

# Delete 'salary' attribute
# del emp1.salary 



# Returns true if 'salary' attribute exists
print (hasattr(e1, 'salary')) 
# Returns value of 'name' attribute
print (getattr(e1, 'name')) 

print(getattr(e1,'salary'))
# Set attribute 'salary' at 8
setattr(e1, 'salary', 7000) 
# Delete attribute 'age'
delattr(e1, 'age') 