# Reverse Arrays
'''
Using slicing operation
Using reverse() method
Using reversed() method
Using for loop'''


# Slicing

import array as arr

numericArray = arr.array('i',[110,220,330,440,550])
print("Original Array:",numericArray)
revArray = numericArray[::-1]
print("Reversed Array:",revArray)


print("****************************************************************")


# Reverse

numericArray = arr.array('i',[110,220,330,440,550])
print("Original Array:",numericArray)

newArray = numericArray.tolist()
newArray.reverse()
revArray = arr.array('i',newArray)
print("Reversed Array:",revArray)

print("****************************************************************")
# Reversed

numericArray1 = arr.array('i',[10,20,30,40,50,60,70])
print("Original Array:",numericArray1)

newArray = list(reversed(numericArray1))

revArray = arr.array('i', newArray)
print("Reversed Array:",revArray)


# For Loop

print("****************************************************************")


c = arr.array('i',[110,220,330,440,550])
d = arr.array('i',)

for i in range(len(c)-1,-1,-1):
    d.append(c[i])

print("Original Array:",c)
print("Reversed Array:",d)