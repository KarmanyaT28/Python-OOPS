# Why Use Self?

# Without self, Python would not know which object's properties you want to access


class Person:
    def __init__(self, age):

        self.age = age

        def printage(self):
            print(self.age)


p1 = Person(22)
p2 = Person(27)

print(p1.age)
print(p2.age)
