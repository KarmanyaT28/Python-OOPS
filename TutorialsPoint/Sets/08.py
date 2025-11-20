# Join Sets in python


s1 = {1,2,3}
s2 = {4,5,6}

s3 = s1 | s2

print(s3)


# Join Python sets using union method


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s3 = s1.union(s2)
print(s3)



# Join python sets using update method


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.update(s2)
print(s1)


# Join Python sets using unpacking operator

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s3 = {*s1, *s2}

print(s3)


# Join python sets using set comprehension

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

joined_set = {x for s in [set1, set2] for x in s}
print(joined_set)


# Join python sets using iterative addition

set1={1,2,3,4,5}
set2={4,5,6,7,8}

joined_set = set()


for element in set1:
    joined_set.add(element)


for element in set2:
    joined_set.add(element)


print(joined_set)