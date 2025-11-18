# Set Operations
from typing import Union

# Union
# Intersection
# Difference
# Symmetric Difference


# Union − It combine elements from both sets using the union() function or the | operator.
#
# Intersection − It is used to get common elements using the intersection() function or the & operator.
#
# Difference − It is used to get elements that are in one set but not the other using the difference() function or the - operator.
#
# Symmetric Difference − It is used to get elements that are in either of the sets but not in both using the symmetric_difference() method or the ^ operator.
#


squared_set = {x**2 for x in range(10)}
print(squared_set)


even_set = {x for x in range(1,11) if x % 2 ==0}
print(even_set)


# Nested Set Comprehensions

nested_set = {(x,y) for x in range(1,3) for y in range(1,3)}

print(nested_set)


# Frozen Sets

my_frozenset = frozenset({1,2,3,4})
print(my_frozenset)
# my_frozenset.add(5)
