# Join Arrays
'''
append()
+ operator()
extend()

'''


# Using append()

import array as arr

a = arr.array('i',[1,2,3,4,5,6,7,8])
b = arr.array('i',[2,7,8,9,0,5,3,2])

for i in range(len(b)):
    a.append(b[i])

print(a)


print("***************************************************")


# Using + operator()


a = arr.array('i',[1,2,3,4,5,6,7,8])
b = arr.array('i',[2,7,8,9,0,5,3,2])
x = a.tolist()
y = b.tolist()
z = x+y
newarr = arr.array('i',z)
print(newarr)


# Using extend method


print("***************************************************")


c = arr.array('i',[1,2,3,4,5,6,7,8])
d = arr.array('i',[2,7,8,9,0,5,3,2])
c.extend(d)
print(c)