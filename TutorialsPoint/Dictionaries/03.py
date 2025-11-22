# You can assign a value to more than one keys in a dictionary, but a key cannot appear more than once in a dictionary


d1 = {
    "Banana":"Fruit",
    "Rose":"Flower",
    "Lotus":"Flower",
    "Mango":"Fruit"
}

d2 = {
    "Fruit":"Banana",
    "Flower":"Rose",
    "Fruit":"Mango",
    "Flower":"Lotus"
}


print(d1)
print(d2)

# Creating a dictionary using curly braces

sports_player = {
    "Name": "Sachin Tendulkar",
    "Age": 48,
    "Sport": "Cricket"
}

print("Dictionary using curly braces: ", sports_player)


# Creating a dictionary using the dict() function

player_info = dict(name="Ben Stokes", age=37, Sport="Cricket")

print("Dictionary using dict(): ", player_info)


# Accessing Dictionary Items

student_info = {
    "Name":"Karmanya",
    "Age": 25,
    "GPA": 4.0
}


# Accessing values using square brackets

name = student_info["Name"]
print("Name: ", name)


# Accessing values using the get() method

age = student_info.get("Age")
print("Age: ", age)



