# Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.


def printme( str ):
    "This prints a passed string into this function"
    print(str)
    return;



printme(str = "My string")


#Another example - order of parameters does not matter

def printinfo(name,age):
    "This prints a passed information into this function"

    print("Name:", name)
    print("Age:", age)
    return;


printinfo(age=50,name="miki")

