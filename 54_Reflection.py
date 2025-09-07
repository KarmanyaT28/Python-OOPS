# Python - Reflection
# ✅ Definition:

# Reflection means examining or modifying the properties, methods, and type of objects at runtime.

# 📝 Notes:

# Functions used:

# type(obj) → returns the class/type.

# id(obj) → memory address.

# dir(obj) → list of attributes/methods.

# getattr(obj, attr) → get attribute value.

# setattr(obj, attr, value) → set attribute.

# hasattr(obj, attr) → check if attribute exists.



class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}"

p = Person("Rajesh")

print(type(p))               # <class '__main__.Person'>
print(hasattr(p, "greet"))   # True
print(getattr(p, "name"))    # Rajesh
setattr(p, "name", "Kiran")
print(p.greet())             # Hello, Kiran
