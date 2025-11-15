# Removing array items in python

# Python arrays are mutable

import array as arr

numericArray = arr.array('i',[111,222,333,2333,4343])

# array.remove(v)
print("Before Removing: ",numericArray)


numericArray.remove(2333)
print("After Removing: ",numericArray)


print("************************************************************************")

# Remove Items from specific indices

# array.pop(i)


numericArray1 = arr.array('i',[111,222,333,444,555])

print("Before Removing: ",numericArray1)

numericArray1.pop(3)

print("After Removing: ",numericArray1)