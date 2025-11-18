# FunctionArguments in python


# def average(a,b):
#     print("The average is " , (a+b)/2)
#
# average(4,6)


def average(a=9,b=3):
    print("The average is ", (a+b)/2)


# average()

average(1,5) # It will ignore the values


average(a=5)
average(b=8)

average(b=21,a=9)

def name(fname,mname="john", lname="whatson"):
    print("Hello", fname, mname, lname)

name("Amy", "Agarwal", "Jain")






def average1(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum = sum+i

    print("The average is ", sum/len(numbers))


average1(1,2,3,4,5,6)


def name(**names):
    print("Hello,", names["fname"], names["mname"], names["lname"])


name(mname="john", lname="whatson", fname="John")





