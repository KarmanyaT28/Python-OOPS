class Myclass:
    x = 5


p1 = Myclass()
print(p1.x)


# delete objects

del p1


# Creating Multiple Objects from the same class

p1 = Myclass()
p2 = Myclass()
p3 = Myclass()

print(p1.x)
print(p2.x)
print(p3.x)

# The pass statement
# class definitions cannot be empty, but if you for some reason have a class
# definition with no content, put in the pass statement to avoid getting an error


class Person:
    pass


