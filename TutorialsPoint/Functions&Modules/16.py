# Function definition
# Default Arguments Example

def showinfo(name,city="hyderabad"):
    "This prints a passed info into this function"

    print("Name:",name)
    print("City:",city)
    return



# Now call showinfo function

showinfo(name="Ansh",city="Delhi")
showinfo(name="shrey")



# Calling Function Without Keyword Arguments


def percent(phy,maths,maxmarks=200):
    val = (phy+maths)*100/maxmarks
    return val


phy=60
maths=70

# function calling with default argument

result = percent(phy,maths)

print("percentage:", result)


phy=40
maths=46


result=percent(phy,maths,100)
print("percentage:", result)



# The code below explains how to use mutable objects as default argument in Python.
#
def fcn(nums, numericlist=[]):
    numericlist.append(nums + 1)
    print(numericlist)


# function calls
fcn(66)
fcn(68)
fcn(70)

