# Nested Dictionaries

# Direct Assignment

# In this approach, we can directly assign dictionaries as values to outer keys within a single dictionary

# Define the outer dictionary

nested_dict = {
    "outer_key1": {"inner_key1":"value1", "inner_key2":"value2"},
    "outer_key2": {"inner_key3":"value3", "inner_key4":"value4"},
}

print(nested_dict)


# Using the loop

# With this method, an empty dictionary is initialized, and then populated with dictionaries as values using a
# loop to define nested dictionaries

nested_dict = {}

outer_keys = ["outer_key1", "outer_key2"]

for key in outer_keys:
    nested_dict[key] = {"inner_key1":"value1", "inner_key2":"value2"}

print(nested_dict)




# Adding Items to a Nested Dictionary in Python


students = {
    "Alice": {"age":21, "major":"Computer Science"},
    "Bob": {"age":25, "major":"Engineering"},
}


# Adding a new-key-value pair to Alice's nested dictionary

students["Alice"]["GPA"] = 3.8

students["Charlie"] = {"age":25, "major":"Mathematics", "GPA":3.0}

print(students)