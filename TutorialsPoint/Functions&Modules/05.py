# Let us now pass a mutable object (such as a list or dictionary) to a function
# It is also passed by reference, as the id() of list before and after passing is same



def testfunction2(arg):
    print("Inside the function:", arg)
    print("ID inside the function:", id(arg))

    arg = arg.append(100)



var = [10,20,30,40]

print("ID before passing:", id(var))
testfunction2(var)
print("list after function call", var)



# also passed by reference, as the id() of list before and after passing is same.