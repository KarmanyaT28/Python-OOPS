# Copy Arrays

import array as arr
'''
We can assign an array to another by using assignment operator (=). 
Such assignment does not create a new array in the memory. Instead, it creates a new reference to the same array
'''
a = arr.array('i',[110,220,330,440,550])
b = a
print("Copied Array:",b)
print(id(a),id(b))

print("********************************************************")
# copy arrays using deep copy


import copy

a1 = arr.array('i',[110,220,330,440,550])
b1 = copy.deepcopy(a1)
print("Copied Array:",b1)

print(id(a1),id(b1))