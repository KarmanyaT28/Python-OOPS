# Accessing array items in python
'''
Using indexing
Using iteration
Using enumerate() function

'''

# Using indexing

import array as arr

# creating an array

arr1 = arr.array('i',[111,222,322,411,544])


# Indexing

print(arr1[0])
print(arr1[1])
print(arr1[2])

print("************************************")
# Iteration

arr2 = arr.array('i',[10,20,40,503,3434,4343])

for item in arr2:
    print(item)

print("************************************")
# Enumerate

arr2 = arr.array('i', [111,222,333,444,555])


# use of enumerate function

for loc, val in enumerate(arr2):
    print(f"Index: {loc}, Value: {val}")