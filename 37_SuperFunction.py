# In Python, super() function allows you to access methods and attributes of the parent 
# class from within a child class.


# In the following example, we create a parent class and access its 
# constructor from a subclass using the super() function.



class ParentDemo:
     def __init__(self, msg):
          self.msg=msg

     def showMessage(self):
          print(self.msg)


class ChildDemo(ParentDemo):
     def __init__(self, msg):
          super().__init__(msg)


# creating instance
obj = ChildDemo("Welcome to Tutorialspoint!!")
obj.showMessage()  