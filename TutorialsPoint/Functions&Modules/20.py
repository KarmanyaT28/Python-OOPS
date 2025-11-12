# Positional-Only Arguments

# we make both the arguments of intr() function as positional-only by putting "/" at the end.


def intr(amt, rate, /):
    val = amt * rate / 100
    return val


print(intr(316200, 4))


# A function may be defined in such a way that it has some keyword-only and some positional-only arguments. Here,
# x is a required positional-only argument, y is a regular positional argument, and z is a keyword-only argument



def myfunction(x, /, y, *, z):
    print(x, y, z)


myfunction(10, y=20, z=30)
myfunction(10, 20, z=30)