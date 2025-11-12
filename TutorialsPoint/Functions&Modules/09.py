# Default Arguments - A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument.


def printinfo(name,age=35):
    "This prints a passed info into this function"

    print("Name: ", name)
    print("Age: ", age)
    return;



printinfo(age=50,name="miki")
printinfo(name="miki")