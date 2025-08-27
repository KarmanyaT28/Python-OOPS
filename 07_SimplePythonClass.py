class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee("Zara", 5000)

emp2 = Employee("Karmanya", 100000000)



emp1.displayEmployee()

emp2.displayEmployee()


print("Total Employees : %d" % Employee.empCount)




# Add an age attribute
emp1.age=23
# Modify age attribute
emp1.age=26
# Delete age attribute
# del emp1.age

print("Age of Employee 1 : %d" % emp1.age)





# Instead of using the normal statements to access attributes, you can also use the following functions −

# getattr(obj, name[, default]) − to access the attribute of object.

# hasattr(obj,name) − to check if an attribute exists or not.

# setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.

# delattr(obj, name) − to delete an attribute.


# Returns true if 'age' attribute exists
hasattr(emp1, 'age')
# Returns value of 'age' attribute
getattr(emp1, 'age')
# Set attribute 'age' as 38
setattr(emp1, 'age', 38)
# Delete attribute 'age'
delattr(emp1, 'age')





