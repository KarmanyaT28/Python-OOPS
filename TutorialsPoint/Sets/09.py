# Python copy sets


# Copy Sets Using the copy() Method



lang1 = {"C", "C++", "Java"}
print("lang1: ",lang1, "id(lang1): ", id(lang1))
lang2 = lang1.copy()
print("lang2: ",lang2, "id(lang2): ", id(lang2))

lang1.add("PHP")

print("After updating lang1")
print("lang1: ", lang1, "id(lang1): ", id(lang1))
print("lang2: ", lang2, "id(lang2): ", id(lang2))




# Copy Sets Using the set() Function

original_set = {1,2,3,4}

copied_set = set(original_set)
print("original_set: ", original_set)
print("copied_set: ", copied_set)


copied_set.add(5)

print("copied_set: ", copied_set)
print("original_set: ", original_set)



# Copy Sets Using Set Comprehension


original_set1 = {1,2,3,4,5,6,7}

copied_set1 = {x for x in original_set1}
print("original_set1: ", original_set1)
print("copied_set1: ", copied_set1)
