# Python variables that are not defined in either local or global scope are called nonlocal variables.


def yourfunction():
   a = 5
   b = 6
   # nested function
   def myfunction():
      # nonlocal function
      nonlocal a
      nonlocal b
      a = 10
      b = 20
      print("variable a:", a)
      print("variable b:", b)
      return a+b
   print (myfunction())
yourfunction()



name = 'TutorialsPoint'
marks = 50
result = True
def mnefunction():
   a = 10
   b = 20
   c = a+b
   print ("globals():", globals())
   print ("locals():", locals())
   return c
mnefunction()