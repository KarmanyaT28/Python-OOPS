# Accessing Items of a Nested Dictionary in Python

# Using Direct Indexing

students = {
    "Alice": {"age":21, "major":"Computer Science"},
    "Bob": {"age":25, "major":"Engineering"},
    "Charlie": {"age":25, "major":"Engineering"},
}



# Access Alice's major

alice_major = students["Alice"]["major"]
print("Alice's major:",alice_major)

# Access Bob's age

bob_age = students["Bob"]["age"]
print("Bob's age:",bob_age)


# Using the get() method

students = {
    "Alice": {"age":21, "major":"Computer Science"},
    "Bob": {"age":25, "major":"Engineering"},
    "Charlie": {"age":25, "major":"Engineering"},
}

# Access alice's major using .get() method

alice_major = students.get("Alice", {}).get("major", "Not Found") #Syntax
print("Alice's major:",alice_major)

# Safety access a non-existing key using .get()

dave_major = students.get("Dave", {}).get("major", "Not Found")

print("Dave's major:",dave_major)


# Deleting a Dictionary from a Nested Dictionary

students = {
    "Alice": {"age":21, "major":"Computer Science"},
    "Bob": {"age":25, "major":"Engineering"},
    "Charlie": {"age":25, "major":"Engineering"},
}


del students["Bob"]

print(students)



# Iterating Through a Nested Dictionary in Python
#


students = {
    "Alice": {"age":21, "major":"Computer Science"},
    "Bob": {"age":25, "major":"Engineering"},
    "Charlie": {"age":25, "major":"Engineering"},
}


# Iterating through the Nested Dictionaries:


for student, details in students.items():
    print(f"Student: {student}")
    for key,value in details.items():
        print(f"{key}: {value}")