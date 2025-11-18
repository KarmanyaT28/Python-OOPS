# Tuple Methods
# The _fields() method
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Access fields using _fields()
print("Fields of p:", p._fields)


# The _replace() method

from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Replace a field value
p2 = p._replace(x=30)

# Access fields
print("p2.x:", p2.x)
print("p2.y:", p2.y)



# The _asdict() method


from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Convert to dictionary
d = p._asdict()
print(d)



# The _make() method


from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Create a new instance using _make()
p2 = Point._make([30, 40])

# Access fields
print("p2.x:", p2.x)
print("p2.y:", p2.y)



# The ** (double star) operator

import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
S = Student('farhan', '23', '2541997')

# initializing iterable
li = ['nishu', '19', '411997']

# initializing dict
di = {'name': "ravi", 'age': 24, 'DOB': '1391997'}

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))