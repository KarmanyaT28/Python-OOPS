# Remove Set Items


# using remove method

my_set = {"Rohan","Physics",21,69.75}
print("My set is", my_set)


my_set.remove("Physics")
print("Set after removing: ", my_set)

# If the element to delete is not found in the set, the remove() method will raise a KeyError exception

# Remove Set Item Using discard() Method

my_set = {"Rohan","Physics",21,69.75}
print("My set is", my_set)


my_set.discard("Physics")
print("Set after removing: ", my_set)


my_set.discard("PHP")
print("Set after removing: ", my_set)




# Remove Set Item Using pop() Method

my_set = {1,2,3,4,5}

removed_element = my_set.pop()

print("Removed element: ", removed_element)
print("Set after removing: ", my_set)



# Remove Set Item Using clear() Method


my_set = {1,2,3,4,5,6}
my_set.clear()

print("Updated set is : ", my_set)



# Remove Items Existing in Both Sets

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# remove those elements from s1 which are present in s2

print("s1 before running difference_update: ", s1)
s1.difference_update(s2)
print("s1 after running difference_update: ", s1)
# print("s1 after running difference_update: ", s1)

# Remove Items Existing in Either of the Sets


set1 = {1,2,3,45}
set2 = {3,4,5,6}

result_set = set1^set2

print("Resulting Set:", result_set)


# Remove Uncommon Set Items

set1 = {1,2,3,4}
set2 = {3,4,5,6}


set1.intersection_update(set2)
print("Se1 1 after keeping only common items: ", set1)



# The intersection() Method


s1 = {1,2,3,4,5}
s2 = {3,4,5,6}

# print("s1 and s2 before intersection: ", s1 & s2)

print ("s1: ", s1, "s2: ", s2)

s3 = s1.intersection(s2)

print("s3 = s1 & s2: ", s3)
# Symmetric Difference Update of Set Items



s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s1.symmetric_difference_update(s2)
print ("s1 after running symmetric difference ", s1)



# Symmetric Difference of Set Items


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.symmetric_difference(s2)
print ("s1 = s1^s2 ", s3)
