# Add Array Elements to Python

'''

Using append()
Using insert()
Using extend()
'''

import array as arr

# append(v)
# We are adding element at the end of the array using append()

a = arr.array('i',[1,2,3])
a.append(10)
print(a)

print("***********************************")
# insert(i,v)
# It is possible to add a new element at the specified index

b = arr.array('i',[1,2,4,5,6])
b.insert(2,3)
print(b)


print("***********************************")
#extend(x)

c = arr.array('i',[1,2,3,4,5,6])
d = arr.array('i',[7,8,9,10])

c.extend(d)
print(c)