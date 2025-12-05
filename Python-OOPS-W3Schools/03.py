# Why use __init__()?

# Without the __init__() method,
# you would need to set properties manually for each object


# Create a class without __init__()

class Person:
    pass

p1 = Person()
p1.name = "John"
p1.age = 22


print(p1.name)
print(p1.age)