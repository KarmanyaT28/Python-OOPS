# Positional-only arguments
# Those arguments that can only be specified by their position in
# the function call is called as Positional-only arguments


# In the following example,
# we have defined two positional-only arguments
# namely "x" and "y". This method should be called with
# positional arguments in the order in which the arguments
# are declared, otherwise, we will get an error.




def posFun(x,y,/,z):
    print(x+y+z)


print("Evaluating positional-only arguments: ")
posFun(33,22,z=11)
# posFun(z=11,22,33)
# posFun(22,z=11,33)