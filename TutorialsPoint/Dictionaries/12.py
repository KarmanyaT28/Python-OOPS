# Copy Dictionaries

# Shallow Copy

# Example-1: Using the copy() method

'''

In the following example, we can see that changing the "age" in the shallow copy does not affect the original.

However, modifying the list in the shallow copy also affects the original because the list is a mutable object and only a reference is copied.



'''

original_dict = {"Name":"Karmanya", "Age":25, "Skills": ["Python","Cybersecurity"]}

shallow_copy = original_dict.copy()


# Modifying the shallow copy

shallow_copy["Age"] = 26
shallow_copy["Skills"].append("Wireshark")


print("Original Dictionary:", original_dict)
print("Shallow copy:", shallow_copy)

print("%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%^%")
# Using the dict() Method

original_dict = {"name":"Karmanya", "Age":25, "Skills": ["Python","Cybersecurity","Shell","Wireshark"]}
shallow_copy = dict(original_dict)





# modifying the shallow copy

shallow_copy["Age"]=31
shallow_copy["Skills"].append("Linux")


print("Original Dictionary:", original_dict)
print("Shallow copy:", shallow_copy)