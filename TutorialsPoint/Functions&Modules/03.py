# In the following example, we are checking the id() of a variable.


def testfunction(arg):
    print("ID inside the function:", id(arg))

var = "Hello"
print("ID before passing:", id(var))
testfunction(var)



# Call by value passes a copy of the data, so the
# original variable is protected from changes, while call by
# reference passes a pointer to the original
# data, allowing the function to modify the original variable.


# Python('s mechanism is pass-by-object-reference (call by sharing), '
# where a copy of the object(')s memory address is passed, causing both the '
# original and formal arguments to initially point to the same object ID.)





# Simple Explanation
# The code first finds the unique ID (memory address) of the string object "Hello" and prints it.
#
# When testfunction(var) is called, Python doesn't copy the string's value; it copies the reference (the ID) to that string object.
#
# Inside the function, when id(arg) is printed, you will see that it's the exact same ID as the one printed before the function call.