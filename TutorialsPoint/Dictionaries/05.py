# Access Dictionary Items


# Example-1 Access Dictionary Items Using Square Brackets []

capitals = {"Maharashtra": "Mumbai", "Uttar Pradesh": "Lucknow", "Madhya Pradesh": "Bhopal"}
print(capitals)

print("Capital of Maharashtra is: ", capitals["Maharashtra"])
print("Capitaal of Uttar Pradesh is: ", capitals["Uttar Pradesh"])


# Example-2 Python raises a KeyError of the kye given inside the square brackets is not present in the dictionary object

capitals1 = {"Maharashtra": "Mumbai", "Uttar Pradesh": "Lucknow", "Madhya Pradesh": "Bhopal", "Karnataka": "Bengaluru"}
print(capitals1)

# print("Capital of Orissa is: ", capitals1["Orissa"])



# Access Dictionary Items Using get() Method


subjects = {"Intro to cybersecurity": "Asynchronous", "Operating Systems": "Asynchronous", "Information Security Management": "Asynchronous"}
print(subjects)

print("The exam for Intro to cybersecurity will be: ", subjects.get("Intro to cybersecurity"))
print("The exam for Operating Systems will be: ", subjects.get("Operating Systems"))


'''Example 2
Unlike the "[]" operator, the get() method doesn't raise error if the key is not found; it return None

'''

subjects1 = {"Fall 2025": "Introduction to cybersecurity", "Spring 2026": "Network Security & Defense", "Fall 2026": "Python & Shell Automation"}
print(subjects1)

Semester = "Spring 2026"

print(f"The subject of {Semester} is: ", subjects1.get('Spring 2026'))


'''
Example 3
The get() method accepts an optional string argument. If it is given, and if the key is not found, this string becomes the return value

'''


subjects1 = {"Fall 2025": "Introduction to cybersecurity", "Spring 2026": "Network Security & Defense", "Fall 2026": "Python & Shell Automation"}
print(subjects1)


print("The subject for Spring 2025 is: ", subjects1.get('Spring 2025', 'Not found'))
