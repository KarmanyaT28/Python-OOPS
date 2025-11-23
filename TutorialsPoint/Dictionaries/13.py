# Deep Copy


import copy
original_dict = {
    "name":"Karmanya",
    "Age":25,
    "Skills": ["Python","Cybersecurity","Shell","Wireshark"],
    "education": {
        "degree":"Masters",
        "field":"Cybersecurity"
    }
}


# creating a deep copy

deep_copy = copy.deepcopy(original_dict)


# Modifying the deep copy

deep_copy["age"] = 26
deep_copy["Skills"].append("Machine Learning")
deep_copy["education"]["degree"] = "Master's"

# Retrieving both dictionaries
print("Original dictionary:", original_dict)
print("Deep copy:", deep_copy)




# Copy Dictionaries Using copy() Method


#Creating a dictionary

dict1 = {"Name":"Krishna","Age":"27","DOY":2000}

dict2 = dict1.copy()

print("dict1:", dict1)
print("dict2:", dict2)