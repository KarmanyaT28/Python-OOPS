# Creating a set in python

my_set = {1, 2, 3, 4, 5}
print (my_set)


# Using the set() Function


my_set = set([1,2,3,4,5])
print (my_set)


# Duplicate Elements in Set

# Sets in Python are unordered collections of unique elements. If you try to create a set with duplicate elements, duplicates will be automatically removed

my_set = {1, 2, 2, 3, 3, 4, 5, 5}
print (my_set)



mixed_set = {1, 'hello', (1,2,3)}
print (mixed_set)


# Adding Elements in a Set

my_set = {1,2,3,4,4,5}

my_set.add(6)
print (my_set)


# Removing elements from a set


my_set = {1,2,3,4,5,6}
my_set.remove(6)
print (my_set)


# Discard

my_set1 = {1,2,3,4,5,6}
my_set1.discard(6)
print (my_set1)



# Membership Testing in a Set


myset = {1,2,3,4,5,6}

if 2 in myset:
    print ("Yes 2 is an element in set")
else:
    print ("No 2 is not an element in set")