# Modifying Dictionary Items

# student_info = {"name": "alice", "age": 22, "major": "Computer Science", "graduation_year": 2026}

student_info = {
    "name": "alice",
    "age": 21,
    "major": "Computer Science"
}



# Modifying an existing key-value pair

# Adding a new key-value pair

print("The modified dictionary is: ", student_info)


# Removing Dictionary Items

student_info1 = {
    "name": "alice",
    "age": 22,
    "major": "Cybersecurity",
    "graduation year": 2027
}

del student_info1["major"]


graduation_year = student_info1.pop("graduation year")

print(student_info1)


# Iterating Through a Dictionary


student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "graduation year": 2028
}


# Iterating through values

for key in student_info:
    print("Keys: ", key, student_info[key])


# Iterating through values

for value in student_info.values():
    print("Values: ", value)


# Iterating through key-value pairs
for key,value in student_info.items():
    print("Key:Value: ", key, value)

'''
There are two important points to remember about dictionary keys −

More than one entry per key not allowed. Which means no duplicate key is allowed. 
When duplicate keys encountered during assignment, the last assignment wins


'''


dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name'])




# Modifying Dictionary Items

# student_info = {"name": "alice", "age": 22, "major": "Computer Science", "graduation_year": 2026}

student_info = {
    "name": "alice",
    "age": 21,
    "major": "Computer Science"
}



# Modifying an existing key-value pair

# Adding a new key-value pair

print("The modified dictionary is: ", student_info)


# Removing Dictionary Items

student_info1 = {
    "name": "alice",
    "age": 22,
    "major": "Cybersecurity",
    "graduation year": 2027
}

del student_info1["major"]


graduation_year = student_info1.pop("graduation year")

print(student_info1)


# Iterating Through a Dictionary


student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science",
    "graduation year": 2028
}


# Iterating through values

for key in student_info:
    print("Keys: ", key, student_info[key])


# Iterating through values

for value in student_info.values():
    print("Values: ", value)


# Iterating through key-value pairs
for key,value in student_info.items():
    print("Key:Value: ", key, value)

'''
There are two important points to remember about dictionary keys −

More than one entry per key not allowed. Which means no duplicate key is allowed.
When duplicate keys encountered during assignment, the last assignment wins


'''


dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
# print ("dict['Name']: ", dict['Name'])





'''
Keys must be immutable. Which means you can use strings, 
numbers or tuples as dictionary keys but something like ['key'] is not allowed.

'''


dict = {'Name': 'Zara', 'Age':7} # Allowed
# dict = {['Name']: 'Zara', 'Age': 7} # Not allowed

print("dict['Name']: ", dict['Name'])


'''

Python Dictionary Methods
Python includes following dictionary methods

1	dict.clear()
Removes all elements of dictionary dict

2	dict.copy()
Returns a shallow copy of dictionary dict

3	dict.fromkeys()
Create a new dictionary with keys from seq and values set to value.

4	dict.get(key, default=None)
For key key, returns value or default if key not in dictionary

5	dict.has_key(key)
Returns true if key in dictionary dict, false otherwise

6	dict.items()
Returns a list of dict's (key, value) tuple pairs

7	dict.keys()
Returns list of dictionary dict's keys

8	dict.setdefault(key, default=None)
Similar to get(), but will set dict[key]=default if key is not already in dict

9	dict.update(dict2)
Adds dictionary dict2's key-values pairs to dict

10	dict.values()
Returns list of dictionary dict's values

Built-in Functions with Dictionaries
Following are the built-in functions we can use with Dictionaries −

Sr.No.	Function with Description
1	cmp(dict1, dict2)
Compares elements of both dict.

2	len(dict)
Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.

3	str(dict)
Produces a printable string representation of a dictionary

4	type(variable)
Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.

'''