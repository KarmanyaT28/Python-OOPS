# issubclass(subclass, superclass)
class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bike:
    pass

# Check subclass relationships
print(issubclass(Car, Vehicle))  # True, because Car inherits Vehicle
print(issubclass(Bike, Vehicle)) # False, Bike doesn't inherit Vehicle
print(issubclass(Vehicle, Vehicle)) # True, a class is considered a subclass of itself


# isinstance(object,Class)

my_car = Car()
my_bike = Bike()

print(isinstance(my_car, Car))       # True, my_car is an instance of Car
print(isinstance(my_car, Vehicle))   # True, Car is a subclass of Vehicle
print(isinstance(my_bike, Vehicle))  # False, Bike is unrelated
