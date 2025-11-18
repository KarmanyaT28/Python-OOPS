# Add an element in SETS

# using add

language = set()

language.add("C")
language.add("C++")
language.add("Java")
language.add("Python")


print("Updated Set :", language)


# using update


my_set = {1,2,3}

my_set.update([4])

print("Updated Set:", my_set)


# Adding any Sequence Object as Set Items


lang1 = {"C","C++","Java","Python"}

lang2 = {"PHP","C#","Perl"}

lang1.update(lang2)

print(lang1)


# a set is constructed from a string, and another string is used as argument for update() method


set1 = set("Hello")
set1.update("World")

print(set1)



# Union Operator

lang1 = {"C","C++","Java","Python"}
lang2 = {"PHP","C#","Perl"}
lang3 = {"SQL","C#"}


combined_set1 = lang1.union(lang2)
combined_set2 = lang2 | lang3


print(combined_set1)
print(combined_set2)


# In the following example, we are defining a list of integers and then using set comprehension to generate a set containing the squares of those integers

numbers = [1,2,3,4,5,6]

squares_set = {num ** 2 for num in numbers}

print(squares_set)






