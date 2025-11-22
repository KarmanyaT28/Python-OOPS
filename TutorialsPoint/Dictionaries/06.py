# Access Dictionary Keys

'''

Example
In this example, we are retrieving all the keys from the dictionary "student_info" using the keys() method

'''

student_info = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 22,
    'gender': 'male',
    'city': 'New York',
    'state': 'NY',
    'country': 'United States',
}

print(student_info)

print("The Keys for the dictionary are : " , student_info.keys())


# Access Dictionary Values


'''

Square Brackets ([]) − By providing the key inside the brackets.

The get() Method − By calling the method with the key as an argument, optionally providing a default value.

The values() Method − which returns a view object containing all the values in the dictionary


'''

'''Example 1
In this example, we are directly accessing associated with the key "name" and "age" using the sqaure brackets'''


fname = student_info["first_name"]
lname = student_info["last_name"]

print(f"Hello {fname} {lname}")



'''

Example 2
In here, we use the get() method to retrieve the value 
associated with the key "major" and provide a default value of "2023" for the key "graduation_year" 

'''


# Creating a dictionary with student information
student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}
# Accessing dictionary values using the get() method
major = student_info.get("major")
# Default value provided if key is not found
grad_year = student_info.get("graduation_year", "2023")

print("Major:", major)
print("Graduation Year:", grad_year)


'''

Example 3
Now, we are retrieving all the values from the dictionary "student_info" using the values() method

'''


all_values  = student_info.values()

print(all_values)


# Access Dictionary Items Using the items() Function



all_items = student_info.items()
print(all_items)