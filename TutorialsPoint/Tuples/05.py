# Unpack tuples


# the term unpacking refers to the process of parsing tuple items in individual variables

x = 10
y = 20

t1 = (x,y)
# t1 = x,y
print(type(t1))


tup1 = (10,20,30)

x,y,z = tup1

print("x: ", x , " y: ", y , " z: ", z)

# this is how the tuple is unpacked in individual variables


# ValueError While Unpacking a tuple

# tup1 = (10,20,30)
# x,y = tup1
# x,y,p,q = tup1


# Unpack tuple items using asterisk (*)

tup1 = (10,20,30)
x, *y = tup1
print("x: ", x, "y: ", y)

# The first value in tuple is assigned to "x", and rest of items to "y" which becomes a list.


tup1 = (10,20,30,40,50,60)
x, *y, z = tup1
print("x: ", x, "y: ", y, "z: ", z)


# What if we add "*" to the first variable?


tup1 = (10,203,303,404,505,600)
*x, y, z = tup1
print("x: ", x, "y: ", y, "z: ", z)