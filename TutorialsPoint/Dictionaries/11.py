# Dictionary View Objects

# The items() method


numbers = {10:"Ten",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}

obj = numbers.items()

print('type of obj: ', type(obj))

print(obj)

print("Update numbers dictionary")
numbers.update({100:"Hundred"})
print(numbers)
print("View automatically updated")
print(obj)


# The keys() Method


obj1=numbers.keys()
print('type of obj1: ', type(obj1))
print(obj1)


obj2 = numbers.values()
print('type of obj2: ', type(obj2))
print(obj2)


# Loop through Dictionaries

# Using a for loop

# Iterating over Keys
student = {"name": "Alice", "Age": 21, "Marks": 51}
for key in student:
    print(key, student[key])


# Iterating over Key-Value Pairs
student = {"name": "Alice", "Age": 21, "Marks": 51, "Major":"Computer"}
for key,value in student.items():
    print(key, value)

# Using dict.items()

student = {"name": "Alice", "Age": 21, "Marks": 51, "Major":"Computer"}

for key,value in student.items():
    print(key, value)



# Using dict.keys()

student = {"name": "Alice", "Age": 21, "Marks": 51}

for key in student.keys():
    print(key)






# Using dict.values()


for value in student.values():
    print(value)