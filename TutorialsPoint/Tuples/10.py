# Python - NamedTuple

from collections import namedtuple
# Point = namedtuple('typename', fieldnames )


# Create a NamedTuple in Python

from collections import namedtuple

Vertex = namedtuple( "Vertex", ["x", "y"])


v = Vertex(100, 100)


print(v.x, v.y)


'''

Accessing by Indexing − You can access the fields using their index, just like a regular tuple.
Accessing by keyname − You can also access the fields using their key names, similar to a dictionary.
Accessing Using getattr() − You can use the getattr() function to access the fields by name.

'''

# Accessing by indexing

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p = Point(10, 20)

print("Point-1", p[0])
print("Point-2", p[1])


# Accessing by keyname



from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Access fields by keyname
print("Point-1:", p.x)
print("Point-2:", p.y)



# Accessing Using getattr()


from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

# Access fields using getattr()
print("getattr(p, 'x'):", getattr(p, 'x'))
print("getattr(p, 'y'):", getattr(p, 'y'))