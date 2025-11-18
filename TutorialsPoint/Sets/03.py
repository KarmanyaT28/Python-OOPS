# Access set items
from _ast import comprehension

# Defining a set

langs = {"C","C++","Java","Python"}

for lang in langs:
    print(lang)



# Access set items using list comprehension

myset = {1,2,3,4,4,5}

accessed_items = [item for item in myset]
print(accessed_items)




# Access subset from a set


import itertools

original_set = {1,2,3,4,4,5}

is_subset = {1,2,3}.issubset(original_set)
print("{1,2} is a subset of the original set: ")


subsets_with_two_elements = [set(subset) for subset in itertools.combinations(original_set, 2)]
print("Subsets with two elements:", subsets_with_two_elements)



