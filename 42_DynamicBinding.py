# In object-oriented programming, the concept of dynamic binding is closely related 
# to polymorphism. In Python, dynamic binding is the process of resolving a method 
# or attribute at runtime, instead of at compile time.

# According to the polymorphism feature, different objects respond differently 
# to the same method call based on their implementations. This behavior is 
# achieved through method overriding, where a subclass 
# provides its implementation of a method defined in its superclass.

# The Python interpreter determines which is the appropriate method or 
# attribute to invoke based on the object's type or class hierarchy at runtime. 
# This means that the specific method or attribute to be called is determined dynamically, 
# based on the actual type of the object.



# class shape:

#     def draw(self):
#         print("Calling to draw a shape from shape class")
#         return
    

# class circle(shape):

#     def draw(self):
#         print("Calling to draw a circle from circle class")
#         return
    



# class rectangle(shape):

#     def draw(self):
#         print("Calling to draw a rectangle from rectangle class")
#         return
    


# c_list = [circle(),rectangle()]

# for c in c_list:
#     c.draw()




#######################################################################################################

# Duck Typing Concept

# Python doesn’t check the class/type of an object before using it.

# Instead, Python checks whether the object has the method/attribute we are trying to use.

# If the method exists → it works.

# If not → it throws an AttributeError.

# The phrase:
# “If it walks like a duck and quacks like a duck, it must be a duck.”



class circle:
    def draw(self):
        print("Draw a circle")


class rectangle:
    def draw(self):
        print("Draw a rectangle")


class area:
    def area(self):
        print("Calculate the area")


# def duck_function(obj):
#     obj.draw()


def duck_function(obj):
    if hasattr(obj, "draw"):   # check if method exists
        obj.draw()
    else:
        print("This object cannot draw")




objects = [circle(), rectangle(), area()] #list created


for obj in objects:
    duck_function(obj)
