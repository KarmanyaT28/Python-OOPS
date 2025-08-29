# The term method resolution order is related to multiple inheritance in Python. 
# In Python, inheritance may be spread over more than one levels. 
# Let us say A is the parent of B, and B the parent for C. 
# The class C can override the inherited method or its object may invoke it as defined in its parent. 
# So, how does Python find the appropriate method to call.


# Each Python has a mro() method that returns the hierarchical order that 
# Python uses to resolve the method to be called. 
# The resolution order is from bottom of inheritance order to top.


# In our previous example, the div_mod class inherits division and modulus classes. 
# So, the mro method returns the order as follows −

# [<class '__main__.div_mod'>, <class '__main__.division'>, <class '__main__.modulus'>, <class 'object'>]
