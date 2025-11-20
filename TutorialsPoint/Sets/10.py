# Set Operators in Python

set1= {1,2,3}
set2= {4,5,6}
set3= {6,7,8,9}
set4 = {9,45,73}


union_set1= set1.union(set2)
union_set2= set3 | set4


print('The union of set1 and set2 is ', union_set1)
print('The union of set3 and set4 is ', union_set2)

# Python Set Intersection Operator (&)


set1 = {1,2,3}
set2 = {3,4,5}
set3 = {6,7,8,9}
set4 = {9,45,73}


intersection_set1= set1.intersection(set2)
intersection_set2= set3 & set4
print('The intersection of set1 and set2 is ', intersection_set1)
print('The intersection of set3 and set4 is ', intersection_set2)




# Python Set Difference Operator (-)


s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {6, 8, 9}
s4 = {9, 8, 73}


difference_set1 = s1.difference(s2)
difference_set2 = s3 - s4

print('The difference of set1 and set2 is ', difference_set1)
print('The difference of set3 and set4 is ', difference_set2)




# Python Set Symmetric Difference Operator


set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}


symmetric_difference_set1 = set1.symmetric_difference(set2)
symmetric_difference_set2 = set3 ^ set4
print('The symmetric difference of set1 and set2 is ', symmetric_difference_set1)
print('The symmetric difference of set3 and set4 is ', symmetric_difference_set2)


# Python Subset Testing Operation


set1 = {1,2}
set2 = {1,2,3,4}
set3 = {64,47,245,48}
set4 = {64,47,3}


is_subset1 = set1.issubset(set2)
is_subset2 = set3 <= set4


print('set1 is a subset of set2', is_subset1)
print('set3 is a subset of set4', is_subset2)