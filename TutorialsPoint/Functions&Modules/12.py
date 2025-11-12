# Arbitrary or Variable-length Arguments

#
# You may need to process a function for more arguments
# than you specified while defining the function.
# These arguments are called variable-length arguments and
# are not named in the function definition, unlike required and default arguments.
#
#


def printinfo(arg1, *vartuple):
    "This prints a variable passed argument"

    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;


printinfo(10)
printinfo(70,60,50)

#
# Order of arguments:
#
# The argument list begins with the positional-only args, followed by the slash (/) symbol.
#
# It is followed by regular positional args that may or may not be called as keyword arguments.
#
# Then there may be one or more args with default values.
#
# Next, arbitrary positional arguments represented by a variable prefixed with single asterisk, that is treated as tuple. It is the next.
#
# If the function has any keyword-only arguments, put an asterisk before their names start. Some of the keyword-only arguments may have a default value.
#
# Last in the bracket is argument with two asterisks ** to accept arbitrary number of keyword arguments.

