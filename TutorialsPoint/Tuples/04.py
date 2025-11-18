# Update Tuples in Python

# By creating a new tuple
T1 = (10,20,30,40)
T2 = ('one', 'two', 'three', 'four')

T1 = T1+T2

print(T1)

# By slicing it into two parts and inserting new elements between the slices



T1 = (10,20,30,40)
new_elements = ('one', 'two', 'three', 'four')

part1 = T1[:2]
part2 = T1[2:]


updated_tuple = part1 + new_elements + part2
print("Original tuple:", T1)
print("Updated tuple:", updated_tuple)
# print(updated_tuple)


# Updating tuples using list comprehension

T1= (10,20,30,40)
# new_elements = ('one', 'two', 'three', 'four')
list_t1 = list(T1)

updated_list = [item + 100 for item in list_t1]

updated_tuple = tuple(updated_list)


print("Original tuple:", T1)
print("Updated tuple:", updated_tuple)


# Updating tuples using append() function



T1 = (10,20,30,40)
list_t1 = list(T1)
new_elements = ('one', 'two', 'three', 'four')

for element in new_elements:
    list_t1.append(element)


updated_tuple = tuple(list_t1)

print("Original tuple:", T1)
print("Updated tuple:", updated_tuple)