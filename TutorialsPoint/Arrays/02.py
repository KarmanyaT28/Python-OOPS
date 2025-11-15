import array as arr

# creating an array with integer type

a = arr.array('i', [1,2,3,4,5])
print(type(a), a)


# creating an array with char type

# a1 = arr.array('u', 'BAT') Deprecated
# print(type(a1), a1)

a1 = arr.array('w', 'BAT')
print(type(a1), a1)


# creating an array with float type

b = arr.array('d', [1.1,2.2,3.3])
print(type(b), b)


# Python array type is decided by a single character Typecode argument.
