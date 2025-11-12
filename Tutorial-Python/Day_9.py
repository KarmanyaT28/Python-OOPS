# Typecasting in python

# Explicit Typecasting

a = "1"
b= "2"

k = "Karmanya "
t = "Tyagi"


print(a+b)
print(k+t)

print(int(a)+int(b))


# The conversion of one data type into the other data type
# Explicit(manually) and Implicit(python itself)


string="15"
number = 7
string_number = int(string)

sum = number + string_number

print("The sum of both the numbers is: ",sum)



# Implicit Typecasting


c = 1.9
d = 8

print(c+d)


# Python converts a smaller datatype to higher datatype to prevent data loss.

