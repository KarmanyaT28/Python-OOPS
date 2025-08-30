# Why Python is Called Dynamically Typed?
# A variable in Python is only a label, or reference to the object stored in the memory, and not a named memory location. Hence, the prior declaration of type is not needed. Because it's just a label, it can be put on another object, which may be of any type.

# In Java, the type of the variable decides what it can store and what not. In Python, it is the other way around. Here, the type of data (i.e. object) decides the type of the variable. To begin with, let us store a string in the variable in check its type.

# >>> var="Hello"
# >>> print ("id of var is ", id(var))
# id of var is 2822590451184
# >>> print ("type of var is ", type(var))
# type of var is <class 'str'>
# So, var is of string type. However, it is not permanently bound. It's just a label; and can be assigned to any other type of object, say a float, which will be stored with a different id() −

# >>> var=25.50
# >>> print ("id of var is ", id(var))
# id of var is 2822589562256
# >>> print ("type of var is ", type(var))
# type of var is <class 'float'>
# or a tuple. The var label now sits on a different object.

# >>> var=(10,20,30)
# >>> print ("id of var is ", id(var))
# id of var is 2822592028992
# >>> print ("type of var is ", type(var))
# type of var is <class 'tuple'>
# We can see that the type of var changes every time it refers to a new object. That's why Python is a dynamically typed language.

# Dynamic typing feature of Python makes it flexible compared to C/C++ and Java. However, it is prone to runtime errors, so the programmer has to be careful.



# Why Python is called Dynamically Typed?

# ✅ Because variable types are determined at runtime (when the code runs), not at compile-time.
# ✅ The same variable name can hold different types of objects at different times.
# ✅ No need to declare type explicitly (int, float, etc.).