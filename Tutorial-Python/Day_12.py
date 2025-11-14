# String Slicing

String1 = "KARMANYATYAGI"

print(String1[0:8])

# 0 is included , 8 is excluded


print(len(String1))

# fruit = "Mango"

# len1 = len(fruit)

# print('Mango is a', len1, 'letter word')

fruit = "Pomegranate"
print(len(fruit))
print(fruit[0:4])
print(fruit[:5])

print(fruit[0:len(fruit)-3])
print(fruit[:len(fruit)-3])
print(fruit[0:-3])

print(fruit[-1:len(fruit)-3]) # Will not make any sense
print(fruit[4:2]) # Will this make any sense


print(fruit[-3:-1])
print(fruit[8:10])


# The first index should always be smaller than the later


