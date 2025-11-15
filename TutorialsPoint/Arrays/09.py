# Accessing a range of array items in python

import array as arr

# creating array

numericArray = arr.array('i', [111,222,333,444,555])


# slicing operation

print(numericArray[2:])
print(numericArray[:3])