# Informal Interface
# In Python, the informal interface refers to a class with methods that can be overridden. 
# However, the compiler cannot strictly enforce the implementation of all the provided methods.

# This type of interface works on the principle of duck typing. It allows us to call any 
# method on an object without checking its type, as long as the method exists.



class demoInterface:
   def displayMsg(self):
      pass

class newClass(demoInterface):
   def displayMsg(self):
      print ("This is my message")
  
# creating instance      
obj = newClass()

# method call
obj.displayMsg()