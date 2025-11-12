# # Anonymous Functions
#
# # The functions are called anonymous when they are not
# # declared in the standard manner by using the def keyword.
# # Instead they are defined using the lambda keyword
#
#
#
# Lambda forms can take any number of arguments but return just one value in the form of an expression. They cannot contain commands or multiple expressions.
#
# An anonymous function cannot be a direct call to print because lambda requires an expression
#
# Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.
#
# Although it appears that lambda's are a one-line version of a function, they are not equivalent to inline statements in C or C++, whose purpose is by passing function stack allocation during invocation for performance reasons.
#


# function definition is here
sum = lambda arg1,arg2: arg1+arg2


print("Value of total:", sum(10,20))
print("Value of total:", sum(99,2428))

